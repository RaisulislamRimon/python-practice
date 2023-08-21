import PySimpleGUI as sg

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
        print('hello')
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()
