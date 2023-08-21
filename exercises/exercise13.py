# import PySimpleGUI as sg
#
# label = sg.Text("What are dolphins?")
# option1 = sg.Radio("Amphibians", group_id="question1")
# option2 = sg.Radio("Fish", group_id="question1")
# option3 = sg.Radio("Mammals", group_id="question1")
# option4 = sg.Radio("Birds", group_id="question1")
#
# window = sg.Window("File Compressor",
#                    layout=[[label],
#                            [option1, option2, option3, option4],
#                            ])
#
# window.read()
# window.close()
#
#
#


import PySimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
quit_btn = sg.Button('Quit')

window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1], [option2], [option3], [option4],
                           [quit_btn]
                           ])

window.read()
window.close()
