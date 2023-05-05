import hashlib
def md5_file(fname):
    # calculate the MD5 checksum of a file
    _hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            _hash.update(chunk)
    return _hash

def sha256_file(fname):
	# calculate the SHA256 checksum of a file
	_hash = hashlib.sha256()
	with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            _hash.update(chunk)
    return _hash
