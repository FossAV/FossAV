import os
import sys

# Installing requirements for the "import" scripts.
def install(requirements_file):
    command = f'pip install -r {requirements_file}'
    os.system(command)

def return_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Checking if modules are installed
try:
    import PySimpleGUI as sg
    import pathlib
    import plyer
except:
    # If not, install requirements
    install(return_path('requirements.txt'))

# Import modules
import PySimpleGUI as sg
import time
import subprocess
import plyer
from plyer import notification

# Set the start locations
fullStart = 'C:\\Users\\' + os.getlogin()
downloadStart = fullStart + '\\Downloads'
testStart = downloadStart + '\\test'
sys32Start = 'C:\\Windows\\System32'
tempStart = os.environ.get('TEMP')

# Notification script
def notify(title, text, time):
    notification.notify(
        title=title,
        message=text,
        app_icon=return_path("Assets\\FossAVIcon.ico"),
        timeout=time,
    )

# Issue removing script
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


# Setting up the window
sg.theme('DarkBlack1')

tab1_layout = [
    [sg.Text("Scan Options:")],
    [sg.Radio('Full Scan', "RADIO1", key='scan1'), sg.Radio('Quick Scan', "RADIO1", key='scan2', default=True)],
    [sg.Button("Scan")],

]

tab2_layout = [
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressbar', pad=((20, 0), (20, 0)), bar_color=('blue',)),],
    [sg.Text("0/0", key='PROGRESS', pad=((20, 0)))],
]

tab3_layout = [
    [sg.Text(text = 'Log:', pad=((20, 0)))],
    [sg.Multiline(size=(100, 25), key='-LOG-', autoscroll=True, disabled=True, pad=((20, 0)))]
]


Stuff = [
    [sg.TabGroup([
        [sg.Tab('Scan', tab1_layout)],
        [sg.Tab('Scan Info', tab2_layout)],
        [sg.Tab('Results', tab3_layout)],
    ], size=(800, 500))],
]

layout = [
    [
        Stuff,
    ]
]

window = sg.Window("FossAV", layout, size=(800, 500))


def runScan(loc):
    subprocess.Popen(["python", "Scan.py", loc])


def endScan():
    elapsed_time = time.time() - start_time
    print("    scan took {:.2f} seconds".format(elapsed_time))


def updateProgress(max_value, value):
    window.read(timeout=0)
    progress_bar = window['progressbar']
    window['progressbar'].update_bar(value, max_value)

def update():
    try:
        window.read(timeout=0)
        with open(return_path('log.txt'), 'r') as f:
            window['-LOG-'].update(value=f.read())
    except:
        pass
    with open(return_path('info.txt'), 'r') as f:
        linething = f.read().splitlines()
        try:
            updateProgress(str(linething[0]), str(linething[2]))
            new_label = str(linething[2]) + '/' + str(linething[0])
            window["PROGRESS"].update(new_label)
        except:
            pass


def startQuick():
    runScan(downloadStart)
    runScan(tempStart)
    runScan(sys32Start)

def startFull():
    runScan(fullStart)

update()

while True:
    event, values = window.read(timeout=50)

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == 'Scan':
        if values['scan1']:
            start_time = time.time()
            startFull()
            sg.popup('Starting Full Scan')
        elif values['scan2']:
            start_time = time.time()
            startQuick()
            sg.popup('Starting Quick Scan')

        scanning = True
        while scanning:
            update()
            with open(return_path('info.txt'), 'r') as f:
                lines = f.read().splitlines()
                try:
                    if lines[1] == 'True':
                        scanning = False
                except:
                    pass
        endScan()
        
window.close()
