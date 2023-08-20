import os
import time
import hashlib
import multiprocessing
from multiprocessing import Pool, Manager
import sys
from pathlib import Path


def return_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def checkIssue():
    try:
        f = open(return_path('output.txt'), 'r')
        if '!' in f.read():
            print('    issues detected!!!')
            print('    removing issue...')
            try:
                with open(return_path('log.txt'), 'r') as f:
                    for line in f:
                        if os.path.exists(return_path(line)):
                            os.remove(return_path(line))
                    os.remove(return_path('log.txt'))
            except:
                print('    could not remove...')
        f.close()
    except:
        print('    error occured.')


def readToSha256(_from):
    global sha256Data
    sha256Data = []
    with open(_from, "r") as f:
        sha256Data = f.read().splitlines()


def readToMd5(_from):
    global md5Data
    md5Data = []
    with open(_from, "r") as f:
        f.read()
        md5Data = f.read().splitlines()


def getSha256(_file):
    global _hash
    sha256_hash = hashlib.sha256()
    with open(_file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    _hash = sha256_hash.hexdigest()
    return(_hash)


def getMd5(_file):
    global _hash
    md5_hash = hashlib.md5()
    with open(_file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    _hash = md5_hash.hexdigest()
    return(_hash)


def scan_directory(directory):
    global amt_scanned
    for root, dirs, files_in_dir in os.walk(directory):
        for file_path in files_in_dir:
            file = os.path.join(root, file_path)
            pool.apply_async(Scan_File, args=(file, sha256Data, md5Data))
            amt_scanned += 1
            amt_scan = str(amt_scanned)
            len_amt = len(amt_scan)
            if '000' in str(amt_scan[len_amt - 3:len_amt]):
                print('    ' + amt_scan)
                
            with open(return_path('info.txt'), 'w') as totalf:
                with open(return_path('output.txt'), 'r') as totalscanf:
                    totalf.write(amt_scan + '\n' + 'False' + '\n' + str(len(totalscanf.read())))
                
            checkIssue()
        for subdir in dirs:
            checkIssue()
            subdir_path = os.path.join(root, subdir)
            scan_directory(subdir_path)
    checkIssue()

def Scan_File(file, sha256Data, md5Data):
    if True:
        getSha256(file)
        if _hash in sha256Data:
            writeExit('!', file)
            os.remove(file)
            return 'virus'
    if True:
        getMd5(file)
        if _hash in md5Data:
            writeExit('!', file)
            os.remove(file)
            return 'virus'
    writeExit('_', '')
    return 'clear'


def waitUntilDone():
    pool.close()
    pool.join()
    

def writeExit(code, file):
    with open('output.txt', 'a') as f:
        f.write(code)
    if code == '!':
        open('log.txt', 'x')
        with open('log.txt', 'a') as f:
            f.write(file)
            


if __name__ == "__main__":
    print('    preparing')
    try:
        input_data = sys.argv[1]
    except:
        pass
    manager = Manager()
    shared_file1 = manager.Namespace()
    shared_file1.path = return_path('output.txt')
    shared_file2 = manager.Namespace()
    shared_file2.path = return_path('log.txt')

    _hash = ''
    with open(return_path('output.txt'), 'w') as f:
        f.truncate(0)
    with open(return_path('log.txt'), 'w') as f:
        f.truncate(0)

    pool = multiprocessing.Pool()
    amt_scanned = 0
    amt_scan = ''
    sha256Data = {}
    md5Data = {}
    full_sha256 = return_path('Hashes/full_sha256.txt')
    full_md5 = return_path('Hashes/full_md5.txt')
    if True:
        print('    adding sha256 database')
        readToSha256(full_sha256)
    if True:
        print('    adding md5 database (this will take a few moments)')
        readToMd5(full_md5)
    try:
        directory = input_data
    except:
        directory = 'C:\\Users\\bramw\\Downloads\\test'
    print('    scan started')
    scan_directory(directory)
    print('    finished scan')
    print('    waiting for results to load...')
    waitUntilDone()
    checkIssue()
    with open(return_path('info.txt'), 'w') as totalf:
        totalf.write(amt_scan + '\n' + 'True')
