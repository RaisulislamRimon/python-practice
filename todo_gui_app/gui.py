# import functions
# import PySimpleGUI as sg  # Part 1 - The import
#
# # Define the window's contents
# layout = [[sg.Text("What's your name?")],  # Part 2 - The Layout
#           [sg.Input(key='-INPUT-')],
#           [sg.Text(size=(40, 1), key='-OUTPUT-')],
#           [sg.Button('Ok'), sg.Button('Quit')]]
#
# # Create the window
# window = sg.Window('Udl App', layout)  # Part 3 - Window Defintion
#
# # Display and interact with the Window
# while True:
#     event, values = window.read()  # Part 4 - Event loop or Window.read call
#     # See if user wants to quit or window was closed
#     if event == sg.WINDOW_CLOSED or event == 'Quit':
#         break
#     # Output a message to the window
#     window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")
#
# # # Do something with the information gathered
# # print('Hello', values[0], "! Thanks for trying PySimpleGUI")
#
# # Finish up by removing from the screen
# window.close()  # Part 5 - Close the Window
#
#
#
#


import functions

import PySimpleGUI as sg

# window = PySimpleGUI.window("My ToDo App", layout="")
layout = [[sg.Text("What is your name? ")],
          [sg.Input()],
          # [sg.Input(key='-INPUT-')],
          # [sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button("Ok"), sg.Button("Quit")],
          ]

window = sg.Window('My ToDo App', layout)

while True:
    event, values = window.read()
    print(event)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # if event == sg.WINDOW_CLOSED or event == 'Quit':
    #     break
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + ", how are you?")
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

print("Hi ", values[0], ", Thanks for using this software")

window.close()
