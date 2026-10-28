"""Adds every mission's package to the local IPFS node, laid out as the site serves it, so
`/ipns/history.sokoly.app/missions/<id>/` on a gateway holds what the site does.

    python3 tools/ipfs.py                  # add and pin; print the root CID and its DNSLink
    python3 tools/ipfs.py --ipns-key KEY   # also publish the root under the node's key KEY

Only the files content.json lists, and content.json itself, are added, with the options
tools/content.py computes their CIDs for; a file whose CID the node gives differently stops
the run. The node keeps them pinned. They stay reachable while a node that has them is
online, so a node that is not always on needs a pinning service as well.

The viewer resolves `ipns://history.sokoly.app/...` through DNSLink: the TXT record
`_dnslink.history.sokoly.app` must read `dnslink=/ipfs/<root>`, or `dnslink=/ipns/<key>`
once the root is published under a key.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import content

SITE = "history.sokoly.app"
ADD = ["ipfs", "add", "--recursive", "--cid-version=1", "--raw-leaves", "--pin=true"]


def stage(into):
    """Hard links (copies across devices) of each package's listed files below `into`."""
    expected = {}
    for package in content.missions():
        listed = json.loads((package / content.MANIFEST).read_text())["files"]
        for relative in [*listed, content.MANIFEST]:
            target = into / "missions" / package.name / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                os.link(package / relative, target)
            except OSError:
                shutil.copyfile(package / relative, target)
            if relative in listed:
                expected[f"missions/{package.name}/{relative}"] = listed[relative]["cid"]
    return expected


def add(staged, expected):
    """The root CID of `staged`, added and pinned, after checking each file's CID."""
    out = subprocess.run([*ADD, "--wrap-with-directory=false", str(staged)], check=True,
                         capture_output=True, text=True, cwd=staged.parent).stdout
    added = {}
    for line in out.splitlines():
        _, cid, path = line.split(" ", 2)
        added[Path(path).relative_to(staged.name).as_posix() if path != staged.name else ""] = cid
    wrong = [f"{path}: node {added.get(path)}, content.json {cid}"
             for path, cid in expected.items() if added.get(path) != cid]
    if wrong:
        sys.exit("CIDs differ from content.json:\n  " + "\n  ".join(wrong))
    return added[""]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--ipns-key", help="publish the root under this key of the node")
    args = parser.parse_args()
    stale = content.check()
    if stale:
        sys.exit("\n".join(stale))
    with tempfile.TemporaryDirectory() as scratch:
        staged = Path(scratch) / "site"
        root = add(staged, stage(staged))
    print(f"root /ipfs/{root}")
    target = f"/ipfs/{root}"
    if args.ipns_key:
        name = subprocess.run(["ipfs", "name", "publish", "--key", args.ipns_key,
                               "--quieter", target], check=True, capture_output=True,
                              text=True).stdout.strip()
        print(f"published under /ipns/{name}")
        target = f"/ipns/{name}"
    print(f"DNSLink: _dnslink.{SITE} TXT \"dnslink={target}\"")


if __name__ == "__main__":
    main()
