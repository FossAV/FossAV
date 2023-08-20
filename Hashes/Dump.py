import requests

print('Downloading…')
lineid = 0
f = open('hashes.txt', 'w')
f.write('')
isFirstLine = True
url = f'https://virusshare.com/hashfiles/unpacked_hashes.md5'
def dump():
        global lineid
        response = requests.get(url, stream=True)
        response.raise_for_status()
        response.encoding = 'utf-8'
        print('starting')
        for line in response.iter_lines(decode_unicode=True):
                if line.startswith('#'):
                        continue
                        if isFirstLine:
                                isFirstLine = False
                        else:
                                line = '\n' + line
                line = '\n' + line
                f.write(line)
                lineid += 1
                lineidstr = str(lineid)
                if '0000' in lineidstr[(len(lineidstr) - 4):len(lineidstr)]:
                        print(str(lineid))

dump()
print(lineid)
print('Download complete')
