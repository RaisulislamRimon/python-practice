import PySimpleGUI as sg

layout = [
    [sg.Text("Enter your name")],
    [sg.Input(), sg.Button("Add to-do")],
    # [sg.Button("Close")]
    [sg.Button("Quit")]
]

window = sg.Window('My App', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()
