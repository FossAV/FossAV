import os

_from = 'full_md5.txt'

with open(_from, "r") as f:
    hashDataList = f.read().splitlines()
    updated_list = [string[:32] for string in hashDataList]
    hashDataList = updated_list

with open('updated.txt', 'w') as f:
    f.writelines(item + "\n" for item in updated_list)
