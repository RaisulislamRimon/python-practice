# simple gui app for file compress
from random import random

import PySimpleGUI as sg
import shutil

layout = [
    # [sg.Text('Select files to compress: ')],
    [sg.Text('Select files to compress: '), sg.Input(), sg.FilesBrowse("Choose")],
    # [sg.Input(), sg.Button("Choose")],
    # [sg.Text('Select destination folder: ')],
    [sg.Text('Select destination folder: '), sg.Input(), sg.FolderBrowse("Choose")],
    # [sg.Input(), sg.Button("Choose")]
    [sg.Button('Compress')],
    [sg.Button('Quit')]

]

window = sg.Window('File Compressor', layout)

while True:
    # print('random: ', random())
    random_file_name = random()
    event, values = window.read()
    # print('event', event)
    if event == 'Compress':
        print('event: ', event)
        print('values: ', values)
        print('values-0: ', values[0])
        print('values-1: ', values[1])
        # shutil.make_archive('output1', 'zip', 'files')
        shutil.make_archive(f"{random_file_name}", 'zip', 'files')
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()
