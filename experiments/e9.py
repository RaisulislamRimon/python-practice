import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name")],
    [sg.Input(key='-INPUT-'), sg.Button("Add to-do")],
    [sg.Text(size=(40, 1), key='-OUTPUT-')],
    # [sg.Button("Close")]
    [sg.Button("Quit")]
]

window = sg.Window('My App', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # print(values['-INPUT-'].capitalize())
    # window['-OUTPUT-'].update('Hi ' + values['-INPUT-'] + ' , how are you?')
    window['-OUTPUT-'].update('Hi ' + values['-INPUT-'].capitalize() + ' , how are you?')

window.close()
