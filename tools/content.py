"""Writes each mission's content manifest, content.json: the length, SHA-256 and IPFS CID of
every file the viewer fetches of the package, so it can take them from IPFS and check them.

    python3 tools/content.py            # every mission
    python3 tools/content.py missions/<id> ...

The CID is the one `ipfs add --cid-version=1 --raw-leaves` gives the file with kubo's default
chunker and balanced layout: 256 KiB raw leaves under dag-pb nodes of at most 174 links. It
is computed here, so writing and checking the manifest needs no IPFS node; adding the
packages to one with those options (tools/ipfs.py) gives the same CIDs.
"""
import base64
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = "content.json"
CHUNK = 256 * 1024
LINKS = 174
RAW, DAG_PB, SHA2_256 = 0x55, 0x70, 0x12


def package_files(package):
    """The files of `package` the viewer fetches: its operation, facts and stories."""
    found = [package / name for name in ("operation.json", "events.jsonl")]
    found += sorted((package / "presentations").glob("*.json"))
    found += sorted(p for p in (package / "segments").rglob("*") if p.is_file())
    return [p for p in found if p.is_file()]


def varint(n):
    out = bytearray()
    while True:
        byte, n = n & 0x7F, n >> 7
        out.append(byte | (0x80 if n else 0))
        if not n:
            return bytes(out)


def field(number, wire, payload):
    """A protobuf field: varints for wire type 0, length-delimited bytes for type 2."""
    key = varint(number << 3 | wire)
    return key + (varint(payload) if wire == 0 else varint(len(payload)) + payload)


def cid_bytes(codec, block):
    return bytes([0x01, codec, SHA2_256, 32]) + hashlib.sha256(block).digest()


def cid_text(raw):
    return "b" + base64.b32encode(raw).decode().lower().rstrip("=")


def node(children):
    """A dag-pb file node over `children`, each (cid, file bytes, subtree bytes): its block,
    the file bytes below it and the bytes of its whole subtree."""
    links = b"".join(field(2, 2, field(1, 2, cid) + field(2, 2, b"") + field(3, 0, tree))
                     for cid, _, tree in children)
    length = sum(size for _, size, _ in children)
    unixfs = field(1, 0, 2) + field(3, 0, length)
    unixfs += b"".join(field(4, 0, size) for _, size, _ in children)
    block = links + field(1, 2, unixfs)
    return cid_bytes(DAG_PB, block), length, len(block) + sum(tree for _, _, tree in children)


def cid(data):
    """The CIDv1 of `data` added with raw leaves and kubo's default chunker and layout."""
    level = [(cid_bytes(RAW, data[i:i + CHUNK]), len(data[i:i + CHUNK]), len(data[i:i + CHUNK]))
             for i in range(0, max(len(data), 1), CHUNK)]
    while len(level) > 1:
        level = [node(level[i:i + LINKS]) for i in range(0, len(level), LINKS)]
    return cid_text(level[0][0])


def manifest(package):
    files = {}
    for path in package_files(package):
        data = path.read_bytes()
        files[path.relative_to(package).as_posix()] = {
            "size": len(data), "sha256": hashlib.sha256(data).hexdigest(), "cid": cid(data)}
    return {"format": "package-content", "version": 1, "files": files}


def text(package):
    return json.dumps(manifest(package), indent=1, ensure_ascii=False) + "\n"


def write(package):
    (package / MANIFEST).write_text(text(package))


def missions():
    return sorted(p for p in (ROOT / "missions").iterdir() if (p / "operation.json").is_file())


def check():
    """Problems: a mission whose content.json is missing or not what its files give."""
    problems = []
    for package in missions():
        written = package / MANIFEST
        if not written.is_file() or written.read_text() != text(package):
            problems.append(f"{package.name}: {MANIFEST} is not what its files give; run "
                            f"python3 tools/content.py {package.relative_to(ROOT)}")
    return problems


if __name__ == "__main__":
    for package in [Path(a).resolve() for a in sys.argv[1:]] or missions():
        write(package)
        print(f"{package.name}: {len(package_files(package))} files")
