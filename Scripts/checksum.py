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

def compsig(*args, **kwargs):
	# args -> [filehash, givenhash]
	# args -> [filepath, hashtype, givenhash]
	if len(args) == 2:
		return args[0] == args[1]
	elif len(args) == 3:
		return args[1](args[0]) == args[2]
	else:
		raise Exception("Invalid arguments provided")