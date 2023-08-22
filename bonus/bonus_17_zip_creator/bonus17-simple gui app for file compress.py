# simple gui app for file compress
# from random import random

import PySimpleGUI as sg
from zip_creator import make_archive

# import shutil
output_label = sg.Text('', key='output_label', text_color='yellow')

layout = [
    # [sg.Text('Select files to compress: ')],
    [sg.Text('Select files to compress: '), sg.Input(), sg.FilesBrowse("Choose", key='files')],
    # [sg.Input(), sg.Button("Choose")],
    # [sg.Text('Select destination folder: ')],
    [sg.Text('Select destination folder: '), sg.Input(), sg.FolderBrowse("Choose", key='folder')],
    # [sg.Input(), sg.Button("Choose")]
    [sg.Button('Compress'), output_label],
    [sg.Button('Quit')]

]

window = sg.Window('File Compressor', layout)

while True:
    # print('random: ', random())
    # random_file_name = random()
    event, values = window.read()
    # print('event', event)
    if event == 'Compress':
        print('event: ', event)
        print('values: ', values)
        # print('values-0(selected files): ', values[0])  # this line &
        # print('values-0(selected files): ', values['Choose'])  # this line are same may be
        # filepaths = values['Choose']
        # filepaths = values['files'] # this is an error
        filepaths = values['files'].split(';')
        print('filepaths', filepaths)
        folder = values['folder']
        print('folder', folder)

        # function calling to make zip files
        message_box = make_archive(filepaths, folder)
        # print(message_box)

        # showing the successful message while make_archive is done
        window['output_label'].update(message_box)

        # print('filepaths', filepaths)
        # print('filepaths', filepaths.split(';'))
        # print('typeof values-0(selected files): ', type(values[0]))
        # print('typeof values-0(selected files): ', type(values['files']))
        # print('values-1(destination): ', values[1])
        # print('values-1(destination): ', values['folder'])
        # shutil.make_archive('output1', 'zip', 'files')
        # this is the line to make zip files
        # shutil.make_archive(f"{random_file_name}", 'zip', 'files')
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # print(event, values)

window.close()
