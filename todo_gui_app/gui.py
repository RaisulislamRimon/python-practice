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
import time

sg.theme('DarkTeal2')
# sg.theme('DarkPurple2')
# sg.theme('DarkPurple4')
# sg.theme('DarkGray')
# sg.theme('Topanga')

clock = sg.Text('', key='clock')
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
delete_button = sg.Button('Delete')
complete_button = sg.Button('Complete')
# error = sg.Text(size=(40, 2), key='-Error-')

# window = PySimpleGUI.window("My ToDo App", layout="")
layout = [[sg.Text("Write a to-do? ")],
          # this is for taking the input from the user
          # [sg.Input()],
          # this is for taking the input from the user
          [sg.Input(key='-INPUT-'), sg.Button("Add to-do", key='add-to-do')],
          # showing the current time here
          [clock],
          # this is for showing the output
          [sg.Text(size=(40, 1), key='-OUTPUT-')],
          # this is the listbox from todos.txt by get_todos function for showing the list
          # [sg.Listbox(values=functions.get_todos(), key='todos', size=(56, 10))],
          [list_box, edit_button, complete_button, delete_button],
          # [delete_button],
          # ok button & quit button
          # [sg.Button("Ok"), sg.Button("Quit")],
          # [sg.Button("Refresh"), sg.Button("Quit")],
          # [error],
          [sg.Button("Quit")]
          ]

# window = sg.Window('My ToDo App', layout)
window = sg.Window('My ToDo App', layout, font=('Consolas', 13))

while True:
    event, values = window.read(timeout=10)
    print('event', event)
    print('values', values)
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    # showing clock
    # window['clock'].update(value=time.strftime('%b %d, %Y; %H:%M:%S %p'))
    window['clock'].update(value=time.strftime('%b %d, %Y; %I:%M:%S %p'))

    # if event == 'Refresh':
    #     functions.get_todos()
    # if event == sg.WINDOW_CLOSED or event == 'Quit':
    #     break
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'].capitalize() + ", how are you?")
    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

    # # while there is an error, it will show the error here
    # window['-Error-'].update('Hey there, ' + values['-Error-'])

    match event:
        case 'add-to-do':
            if not values['-INPUT-']:
                error = 'Write a to-do first'
                # showing error message with popup
                sg.popup(error, font=('Consolas', 13))
                continue
            # print('get_todos()')
            todos = functions.get_todos()
            new_todos = values['-INPUT-'] + '\n'
            # print(todos)
            # print(new_todos)
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(todos)
            # showing the last added to-do to the gui all on a sudden
            # updated_todos = functions.get_todos()
        case 'Edit':
            # print('edit button clicked')
            # if user input anything & doesn't select any todos from the list to edit,
            # then user will see this
            if not values['todos']:
                # print('Select todos to edit')
                error = 'Select todos to edit'
                # showing error message with popup
                sg.popup(error, font=('Consolas', 13))
                continue
            todos_to_edit = values['todos'][0]
            # print(todos_to_edit)
            new_edited_todo = values['-INPUT-'] + '\n'
            # print(new_edited_todo)
            todos = functions.get_todos()
            index = todos.index(todos_to_edit)
            # print(index)
            todos[index] = new_edited_todo
            functions.write_todos(todos)
            window['todos'].update(todos)
        case 'Delete':
            if not values['todos']:
                error = 'Select todos to Delete'
                # showing error message with popup
                sg.popup(error, font=('Consolas', 13))
                continue
            todos_to_delete = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(todos_to_delete)
            # print(index)
            todos_after_deleted = todos.pop(index)
            functions.write_todos(todos)
            window['todos'].update(todos)
            # print('delete btn clicked')
        case 'Complete':
            if not values['todos']:
                error = 'Select todos to Complete'
                # showing error message with popup
                sg.popup(error, font=('Consolas', 13))
                continue
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['-INPUT-'].update('')
        case 'todos':
            if not values['todos']:
                continue
            window['-INPUT-'].update(values['todos'][0])
# print("Hi ", values['-INPUT-'], ", Thanks for using this software")
#

# while there is an error, it will show the error here
# window['-Error-'].update('Hey there, ' + values['-Error-'])
# print("Hi ", values['-Error-'], ", Thanks for using this software")

window.close()
