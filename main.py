# print("Enter a todo: ")
# name = input("This is the input area: ")
# print(name)
#
# if name == 'hi':
#     print("input correct")
# # elif print('wrong input')
#

# user_prompt = "Enter a todo: "
# text = input(user_prompt)
# print(text)

#
# user_prompt = "Enter a todo: "
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
#
# print(todo1)
# print(todo2)
# print(todo3)
#
# todo = [todo1, todo2, todo3]
# todo1 = [todo1, todo2, todo3, "new sentence"]
# print(todo)     # ['1', '2', '3']
# print(type(todo))   # <class 'list'>
# print(type(todo1))   # <class 'list'>
#
# todo1 = {todo1, todo2, todo3}
# print(todo1)    # {'1', '2', '3'}
# print(type(todo1))  # <class 'set'>


# user_prompt = input("write something: ")
# print(user_prompt)
# print(len(user_prompt))  # check length of given input

# check length

# text = input("Enter a title: ")
# length = len(text)
# print(length)

# text = input('enter somthing: ')
# length = len(text)
# print('total length/character of the given string/input is : ', length)
#

# answers = ['Yes', 'No', 'Yes', 'No', 'No']

# my_answer = input("What is your answer?")
# answers = ['Yes', 'No', 'Yes' 'No' ,my_answer]
# print(answers)
# print(len(answers))
# print(type(answers))

# my_answer = input('What is your answer?')
# answers = ['Yes', 'No', 'Yes', 'No', my_answer]

# my_answer = input["What is your answer?"]
# my_answer = input("What is your answer?")
# answers = ['Yes', 'No', 'Yes', 'No', my_answer]

# greeting1 = "Hi"
# greeting2 = "Hello  "
# print(greeting1, greeting2)

# today greeting = "Hello"
# today_greeting = "Hello"

# greeting = "Hello"
# greeting = "Hi"
#
# print(greeting)
# print(greeting, greeting)


# take unlimited input from the user

# user_prompt = 'write something: '
# # input(user_prompt)
# while 2 > 1:
#     todo1 = input(user_prompt)
#     print(todo1)
#     if (todo1 == 'q'):
#         quit()


# take unlimited input from the user

# user_prompt = 'write something: '
# # input(user_prompt)
# while True:
#     todo1 = input(user_prompt)
#     print(todo1)
#     if (todo1 == 'q'):
#         quit()
#


# method

# while True:
#     todo = input('enter todo: ')
#     todos = [todo]
#     print(todos)
#     # print(type(todos))


# storing user inputs repeatedly

# todos = []
#
# while True:
#     todo = input('enter something: ')
#     # todos.append()  # this line shows error
#     todos.append(todo)
#     print(todos)
#     print(type(todos))
#     print('Capitalize : ', todo.capitalize())


# todos = []
# while True:
#     user_action = input('Type add or show: ')
#     match user_action:
#         case 'add':
#             todo = input('enter a todo: ')
#             todos.append(todo)
#         case 'show':
#             print(todos)
#

#
#
# import tkinter as tk
#
# def hello_world():
#   print("Hello, world!")
#
# window = tk.Tk()
# window.title("My Application")
#
# button = tk.Button(window, text="Click Me", command=hello_world)
# button.pack()
#
# window.mainloop()
#
#


#
# import tkinter as tk
#
# todos = []
#
# def add_todo():
#   todo = text_box.get()
#   todos.append(todo)
#   text_box.delete(0, tk.END)
#
# def show_todos():
#   text_box.delete(0, tk.END)
#   text_box.insert(0, todos)
#
# window = tk.Tk()
# window.title("My To-Do List")
# window.geometry("500x400")
#
# text_box = tk.Entry(window)
# text_box.pack()
#
# button_add = tk.Button(window, text="Add Todo", command=add_todo)
# button_add.pack()
#
# button_show = tk.Button(window, text="Show Todos", command=show_todos)
# button_show.pack()
#
# window.mainloop()
#

#
# import tkinter as tk
#
# todos = []
#
# def add_todo():
#   todo = text_box.get()
#   if not todo:
#     return
#   todos.append(todo)
#   text_box.delete(0, tk.END)
#
# def show_todos():
#   text_box.delete(0, tk.END)
#   text_box.insert(0, "\n".join(todos))
#
#   label = tk.Label(window, text="Todos: {}".format(todos))
#   label.pack(side="bottom")
#
#   new_label = tk.Label(window, text="Results: {}".format(todos))
#   new_label.pack(side="bottom")
#
# window = tk.Tk()
# window.title("My To-Do List")
# window.geometry("500x400")
#
# text_box = tk.Entry(window)
# text_box.pack()
#
# button_add = tk.Button(window, text="Add Todo", command=add_todo)
# button_add.pack()
#
# button_show = tk.Button(window, text="Show Todos", command=show_todos)
# button_show.pack()
#
# window.mainloop()
#


# todos = []
# while True:
#     user_action = input('type add or show or exit: ')
#
#     match user_action:
#         case 'add':
#             todo = input('type your todo: ')
#             todos.append(todo)
#         case 'show':
#             print(todos)
#         case 'exit':
#             exec()

# todos = []
# for item in todos:
#     print(item)


# # todos = [1, 2, 3]
# todos = []
# while True:
#     user_action = input('type add or show or exit: ')
#
#     match user_action:
#         case 'add':
#             todo = input('type your todo: ')
#             todos.append(todo)
#         case 'show':
#             # print(todos) # [1, 2, 3]
#             print(len(todos))
#             if len(todos) == 0:
#                 print('nothing...')
#             for item in todos:
#                 item = item.title()
#                 print(item)     # 1
#                                 # 2
#                                 # 3
#         case 'exit':
#             break
#         case _:
#             print('do not enter random input')
#
# print("bye")
#


#
# # todos = [1, 2, 3]
# todos = []
# while True:
#     user_action = input('type add, show, edit or exit: ')
#
#     match user_action:
#         case 'add':
#             todo = input('type your todo: ')
#             todos.append(todo)
#         case 'show':
#             # print(todos) # [1, 2, 3]
#             print('total items: ', len(todos))
#             if len(todos) == 0:
#                 print('nothing...')
#             for item in todos:
#                 item = item.title()
#                 print(item)     # 1
#                                 # 2
#                                 # 3
#         case 'edit':
#             print('Got it')
#             number = int(input('Number of the todo to edit: '))
#             number = number - 1
#             print(number)
#             existing_todo = todos[number]
#             print('older value: ', existing_todo)
#             new_todo = input('enter new todo: ')
#             print('new value: ', new_todo)
#             todos[number] = new_todo
#
#         case 'exit':
#             break
#         case _:
#             print('do not enter random input')
#
# print("bye")
#


#
# a = input('Enter some input: ')
# b = int(a)
# print(type(a))
# print(type(b))
#


#
# myList = ['a', 'b', 'c']
# print(myList)
# print(myList[0])
# print(myList[1])
# print(myList[1] == 'b')
# print(myList.index('b'))
# # setting items
# myList.__setitem__(1, 'd')
# print(myList)
# # setting items
# myList[1] = 'e'
# print(myList)
# # getting items
# # myList.__getitem__(2)
# print(myList.__getitem__(2))
# print(myList)
#

#
# fileNames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
# newfileNames = []
# for fileName in fileNames:
#     # print('fileName: ', fileName)
#     # newfileName = fileName.replace('.', '_')
#     newfileName = fileName.replace('.', '_', 1)
#     newfileNames.append(newfileName)
# print(newfileNames)
# print(type(newfileNames))
# for newfileName in newfileNames:
#     print(newfileName)
#


#
# # todos = [1, 2, 3]
# todos = []
# while True:
#     user_action = input('type add, show, complete, edit or exit: ')
#
#     match user_action:
#         case 'add':
#             todo = input('type your todo: ')
#             todos.append(todo)
#         case 'show':
#             # print(todos) # [1, 2, 3]
#             print('total items: ', len(todos))
#             if len(todos) == 0:
#                 print('nothing...')
#
#             for index, item in enumerate(todos):
#                 # print(index + 1, ". ", item)
#                 print(f"{index + 1}.{item}")
#
#             for item in todos:
#                 item = item.title()
#                 print(item)     # 1
#                                 # 2
#                                 # 3
#         case 'edit':
#             print('Got it')
#             number = int(input('Number of the todo to edit: '))
#             number = number - 1
#             print(number)
#             existing_todo = todos[number]
#             print('older value: ', existing_todo)
#             new_todo = input('enter new todo: ')
#             print('new value: ', new_todo)
#             todos[number] = new_todo
#
#         case 'complete':
#             number = int(input('number of the todo to complete: '))
#             todos.pop(number - 1)
#
#         case 'exit':
#             break
#         case _:
#             print('do not enter random input')
#
# print("bye")
#


#
# a = ['x', 'y', 'z']
# print(a)
# for index, data in enumerate(a):
#     print(index, data)
# # print(enumerate(a))   # <enumerate object at 0x000000C95C5254E0>
# # a = list(a)
# # print(a)
#


#
#
# buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
# for first, second, third in buttons:
#     print(first, second, third)
#


#
# name = input("Enter your name: ")
# print(f"Your name is {name}.")
#


#
# todos = []
# while True:
#     user_action = input('type add, show, complete, edit or exit: ')
#
#     match user_action:
#         case 'add':
#             todo = input('type your todo: ') + '\n'
#             # read files from older docuements
#             file = open('todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#
#             todos.append(todo)
#
#             # save file in txt document
#             file = open('todos.txt', 'w')
#             file.writelines(todos)
#             file.close()
#         case 'show':
#             # print(todos) # [1, 2, 3]
#             print('total items: ', len(todos))
#             if len(todos) == 0:
#                 print('nothing...')
#
#             for index, item in enumerate(todos):
#                 # print(index + 1, ". ", item)
#                 print(f"{index + 1}.{item}")
#
#             for item in todos:
#                 item = item.title()
#                 print(item)     # 1
#                                 # 2
#                                 # 3
#         case 'edit':
#             print('Got it')
#             number = int(input('Number of the todo to edit: '))
#             number = number - 1
#             print(number)
#             existing_todo = todos[number]
#             print('older value: ', existing_todo)
#             new_todo = input('enter new todo: ')
#             print('new value: ', new_todo)
#             todos[number] = new_todo
#
#         case 'complete':
#             number = int(input('number of the todo to complete: '))
#             todos.pop(number - 1)
#
#         case 'exit':
#             break
#         case _:
#             print('do not enter random input')
#
# print("bye")
#
#


#
# while True:
#     user_action = input('type add, show, complete, edit or exit: ')
#
#     match user_action:
#         case 'add':
#             todo = input('type your todo: ') + '\n'
#             # read files from older docuements
#             # file = open('todos.txt', 'r')
#             # todos = file.readlines()
#             # file.close()
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             todos.append(todo)
#
#             # save file in txt document
#             # file = open('todos.txt', 'w')
#             # file.writelines(todos)
#             # file.close()
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         case 'show':
#             # read files from older docuements - analog system
#             # file = open('todos.txt', 'r')
#             # todos = file.readlines()
#             # file.close()
#
#             # updated system to access file
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             print('total items: ', len(todos))
#
#             if len(todos) == 0:
#                 print('nothing...')
#             for index, item in enumerate(todos):
#                 item = item.strip('\n')
#                 print(f"{index + 1}.{item}")
#             for item in todos:
#                 item = item.title()
#         case 'edit':
#             print('Got it')
#             number = int(input('Number of the todo to edit: '))
#             number = number - 1
#             print(number)
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             existing_todo = todos[number]
#             print('older value: ', existing_todo)
#             new_todo = input('enter new todo: ')
#             print('new value: ', new_todo)
#
#             todos[number] = new_todo + '\n'
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         case 'complete':
#             number = int(input('number of the todo to complete: '))
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             index = number - 1
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#
#             message = f"Todo {todo_to_remove} was removed from the list."
#             print(message)
#
#         case 'exit':
#             break
#         case _:
#             print('do not enter random input')
#
# print("bye")
#


#
#
# while True:
#     user_action = input('type add, show, complete, edit or exit: ')
#
#     # if 'add' in user_action or 'new' in user_action or 'more' in user_action:
#     # if 'add' in user_action and 'new' in user_action:
#     # if 'add' not in user_action:
#     if 'add' in user_action:
#         # todo = input('type your todo: ') + '\n'
#         todo = user_action[4:] + '\n'
#         # read files from older docuements
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#         todos.append(todo)
#
#         # save file in txt document
#         # file = open('todos.txt', 'w')
#         # file.writelines(todos)
#         # file.close()
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#
#     elif 'show' in user_action:
#         # read files from older docuements - analog system
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         # updated system to access file
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#         print('total items: ', len(todos))
#
#         if len(todos) == 0:
#             print('nothing...')
#         for index, item in enumerate(todos):
#             item = item.strip('\n')
#             print(f"{index + 1}.{item}")
#             for item in todos:
#                 item = item.title()
#
#     elif 'edit' in user_action:
#         print('Got it')
#         # number = int(input('Number of the todo to edit: '))
#         number = int(user_action[5:])
#         number = number - 1
#         print(number)
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#         existing_todo = todos[number]
#         print('older value: ', existing_todo)
#         new_todo = input('enter new todo: ')
#         print('new value: ', new_todo)
#
#         todos[number] = new_todo + '\n'
#
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#
#     elif 'complete' in user_action:
#         # number = int(input('number of the todo to complete: '))
#         number = int(user_action[9:])
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#         index = number - 1
#         if len(todos) > index:
#             print('item is not found')
#             # break
#         else:
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)
#
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#
#         message = f"Todo {todo_to_remove} was removed from the list."
#         print(message)
#
#     elif 'exit' in user_action:
#         break
#     elif '_' in user_action:
#         print('do not enter random input')
#     else:
#         print('command is not valid')
#
# print("bye")
#
#


#
# while True:
#     user_action = input('type add, show, complete, edit or exit: ')
#     user_action = user_action.strip()
#
#     # if 'add' in user_action or 'new' in user_action or 'more' in user_action:
#     # if 'add' in user_action and 'new' in user_action:
#     # if 'add' not in user_action:
#     # if 'add' in user_action:
#     if user_action.startswith('add'):
#         # todo = input('type your todo: ') + '\n'
#         todo = user_action[4:]
#         # read files from older docuements
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#         todos.append(todo + '\n')
#
#         # save file in txt document
#         # file = open('todos.txt', 'w')
#         # file.writelines(todos)
#         # file.close()
#         with open('todos.txt', 'w') as file:
#             file.writelines(todos)
#
#     # elif 'show' in user_action:
#     elif user_action.startswith('show'):
#         # read files from older docuements - analog system
#         # file = open('todos.txt', 'r')
#         # todos = file.readlines()
#         # file.close()
#
#         # updated system to access file
#         with open('todos.txt', 'r') as file:
#             todos = file.readlines()
#
#         print('total items: ', len(todos))
#
#         if len(todos) == 0:
#             print('nothing...')
#         for index, item in enumerate(todos):
#             item = item.strip('\n')
#             print(f"{index + 1}.{item}")
#             for item in todos:
#                 item = item.title()
#
#     # elif 'edit' in user_action:
#     elif user_action.startswith('edit'):
#         try:
#             print('Got it')
#             # number = int(input('Number of the todo to edit: '))
#             number = int(user_action[5:])
#             number = number - 1
#             print(number)
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             existing_todo = todos[number]
#             print('older value: ', existing_todo)
#             new_todo = input('enter new todo: ')
#             print('new value: ', new_todo)
#
#             todos[number] = new_todo + '\n'
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#         except ValueError:
#             print('Your command is not valid.')
#             # user_action = input('type add, show, complete, edit or exit: ')
#             # user_action = user_action.strip()
#             continue
#
#
#     # elif 'complete' in user_action:
#     elif user_action.startswith('complete'):
#         try:
#             # number = int(input('number of the todo to complete: '))
#             number = int(user_action[9:])
#
#             with open('todos.txt', 'r') as file:
#                 todos = file.readlines()
#
#             index = number - 1
#             # if len(todos) > index:
#             #     print('item is not found')
#             #     # break
#             # else:
#             todo_to_remove = todos[index].strip('\n')
#             todos.pop(index)
#
#             with open('todos.txt', 'w') as file:
#                 file.writelines(todos)
#
#             message = f"Todo {todo_to_remove} was removed from the list."
#             print(message)
#         except IndexError:
#             print('command is not valid')
#             continue
#
#
#     # elif 'exit' in user_action:
#     elif user_action.startswith('exit'):
#         break
#     # elif '_' in user_action:
#     elif user_action.startswith('_'):
#         print('do not enter random input')
#     else:
#         print('command is not valid')
#
# print("bye")
#


#
# custom function

def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# def set_todos():
#     with open('todos.txt', 'w') as file:
#         todos = file.writelines()
#     return todos


while True:
    user_action = input('type add, show, complete, edit or exit: ')
    user_action = user_action.strip()

    # if 'add' in user_action or 'new' in user_action or 'more' in user_action:
    # if 'add' in user_action and 'new' in user_action:
    # if 'add' not in user_action:
    # if 'add' in user_action:
    if user_action.startswith('add'):
        # todo = input('type your todo: ') + '\n'
        todo = user_action[4:]
        # read files from older docuements
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()
        todos = get_todos()

        todos.append(todo + '\n')

        # save file in txt document
        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # elif 'show' in user_action:
    elif user_action.startswith('show'):
        # read files from older docuements - analog system
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # updated system to access file
        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()
        todos = get_todos()

        print('total items: ', len(todos))

        if len(todos) == 0:
            print('nothing...')
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item}")
            for item in todos:
                item = item.title()

    # elif 'edit' in user_action:
    elif user_action.startswith('edit'):
        try:
            print('Got it')
            # number = int(input('Number of the todo to edit: '))
            number = int(user_action[5:])
            number = number - 1
            print(number)

            # with open('todos.txt', 'r') as file:
            #     todos = file.readlines()
            todos = get_todos()

            existing_todo = todos[number]
            print('older value: ', existing_todo)
            new_todo = input('enter new todo: ')
            print('new value: ', new_todo)

            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Your command is not valid.')
            # user_action = input('type add, show, complete, edit or exit: ')
            # user_action = user_action.strip()
            continue


    # elif 'complete' in user_action:
    elif user_action.startswith('complete'):
        try:
            # number = int(input('number of the todo to complete: '))
            number = int(user_action[9:])

            # with open('todos.txt', 'r') as file:
            #     todos = file.readlines()
            todos = get_todos()

            index = number - 1
            # if len(todos) > index:
            #     print('item is not found')
            #     # break
            # else:
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print('command is not valid')
            continue


    # elif 'exit' in user_action:
    elif user_action.startswith('exit'):
        break
    # elif '_' in user_action:
    elif user_action.startswith('_'):
        print('do not enter random input')
    else:
        print('command is not valid')

print("bye")
