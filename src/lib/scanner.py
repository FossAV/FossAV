from pathlib import Path

NAME_FLAGS = [
    ".vbs",
    "virus",
    "trojan",
    "malware",
    "ransom",
    "ransomware",
    "worm",
    ".bat",
]


def scan_dir(path):
    return [(_path, scan_all(_path)) for _path in Path(path).rglob("*")]


def scan_all(path):
    e = []
    e.append(scan_name(path))
    return any(e)


def scan_name(path):
    return any(s in path for s in NAME_FLAGS)
