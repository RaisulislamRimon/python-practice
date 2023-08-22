import PySimpleGUI as sg

import zip_extractor_main

sg.theme("Black")

label1 = sg.Text("Select archive dir : ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

layout = [
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [extract_button, output_label]
]

window = sg.Window("Archive Extractor", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # print('event', event)
    # print('values', values)
    archive_paths = values['archive']
    extract_destination = values['folder']

    # print(archive_paths)
    # print(extract_destination)
    zip_extractor_main.extract_archive(archive_paths, extract_destination)

    window['output'].update(value="Extraction completed")

window.close()
