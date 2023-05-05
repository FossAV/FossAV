import sys, os, shutil

from pathlib import Path


def checkSketchy(sourcePath):
    flags = [
        ".vbs",
        "virus",
        "trojan",
        "malware",
        "ransom",
        "ransomware",
        "worm",
        ".bat",
    ]
    copyFile(sourcePath, r"scan.txt")
    end = 0
    fileToList("scan.txt", "no")
    if any(substring in str(sourcePath) for substring in flags):
        print("Possible Threat")
        end = 1
    if any(item in myFile for item in evilCode):
        print("Possible Threat")
        end = 1
    os.remove("scan.txt")
    if end == 0:
        print("Nothing Detected")


def copyFile(location, destination):
    src_path = os.path.normpath(location)
    dst_path = destination
    shutil.copy(src_path, dst_path)


def fileToList(fileName, flag):
    filename = os.path.normpath(fileName)
    with open(filename, "r", encoding="utf8") as infile:
        lines = infile.readlines()
        for line in lines:
            if flag == "no":
                myFile.append(str(line))
            else:
                evilCode.append(str(line))


def importFilesFromFlags():
    entries = os.listdir("Flags/")
    repeat = len(entries)
    for i in range(repeat):
        itemInList = entries[int(i)]
        fileToList(f"Flags/{str(itemInList)}", "yes")


evilCode = []
myFile = []
importFilesFromFlags()

while True:
    fileLoc = input("File Location: ")
    checkSketchy(fileLoc)
