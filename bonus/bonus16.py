# simple gui app for file compress

import PySimpleGUI as sg
import shutil

layout = [
    # [sg.Text('Select files to compress: ')],
    [sg.Text('Select files to compress: '), sg.Input(), sg.Button("Choose")],
    # [sg.Input(), sg.Button("Choose")],
    # [sg.Text('Select destination folder: ')],
    [sg.Text('Select destination folder: '), sg.Input(), sg.Button("Choose")],
    # [sg.Input(), sg.Button("Choose")]
    [sg.Button('Compress')]

]

window = sg.Window('File Compressor', layout)

while True:
    event, values = window.read()
    # print(event)
    if event == 'Compress':
        shutil.make_archive('output1', 'zip', 'files')
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()
