import os
import sys

# Installing requirements for the "import" scripts.
def install(requirements_file):
    command = f'pip install -r {requirements_file}'
    os.system(command)

def return_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

install(return_path('requirements.txt'))


import time
import subprocess
import plyer
from plyer import notification


fullStart = 'C:\\Users\\' + os.getlogin()

downloadStart = fullStart + '\\Downloads'
testStart = downloadStart + '\\test'

sys32Start = 'C:\\Windows\\System32'

tempStart = os.environ.get('TEMP')


def notify(title, text, time):
    notification.notify(
        title=title,
        message=text,
        app_icon=return_path("Assets\\FossAVIcon.ico"),
        timeout=time,
    )


def checkForIssues():
    try:
        f = open(return_path('output.txt'), 'r')
        if '!' in f.read():
            print('    issues detected!!!')
            notify('Issue Found!', 'FossAV Found An Issue!', 5)
            print('    removing issue...')
            try:
                with open(return_path('log.txt'), 'r') as f:
                    for line in f:
                        if os.path.exists(return_path(line)):
                            os.remove(return_path(line))
                os.remove(return_path('log.txt'))
            except:
                print('    could not remove...')
        else:
            print('    fossav found no issues')
        f.close()
    except:
        print('    error occured.')


def runScan(startloc):
    process = subprocess.Popen(["python", return_path("Scan.py"), startloc])
    process.wait()
    checkForIssues()


def cmd(command):
    if inp == command:
        return True
    else:
        return False

def endScan():
    elapsed_time = time.time() - start_time
    print("    scan took {:.2f} seconds".format(elapsed_time))


def printCom(commandName, commandDescription):
    print(f"        {commandName}    <{commandDescription}>")


def printCommands():
    print('    commands:')
    printCom('full', 'does a full scan')
    printCom('scan', 'does a quick scan in common virus locations')
    printCom('view', 'view scan results')
    printCom('test', 'makes sure everything is working correctly')
    print()

def doCommand():
    if cmd('help'):
        printCommands()
    if cmd('full'):
        runScan(fullStart)
        
        endScan()
    if cmd('scan'):
        runScan(downloadStart)
        runScan(tempStart)
        runScan(sys32Start)
        
        endScan()
    if cmd('test'):
        runScan(testStart)
        
        endScan()

inp = ''

start_time = 0


print('Welcome To FossAV')
print('    "help" for more commands')
print()

while True:
    inp = input('>>> ')
    start_time = time.time()
    doCommand()
