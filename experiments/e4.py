#
#
#
#
#
#

#
#
# custom function

# def get_todos(filepath):
# def get_todos(filepath):   # TypeError: get_todos() missing 1 required positional argument: 'filepath'
def get_todos(filepath='todos.txt'):
    """ Read a text file and return the list of
    to-do items. """
    # filepath = 'todos.txt'
    # with open('todos.txt', 'r') as file_local:
    with open(filepath, 'r') as file_local:
        # return filepath
        todos_local = file_local.readlines()
    return todos_local


# document the code #doc-strings
# print(help(get_todos))
# this is the result
# Help on function get_todos in module __main__:
#
# get_todos(filepath='todos.txt')
#     Read a text file and return the list of
#     to-do items.
#
# None


# def write_todos(filepath, todos_arg):
# def write_todos(filepath='todos.txt', todos_arg):
def write_todos(todos_arg, filepath='todos.txt'):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(help(write_todos))

# text = """
# lorem ipsum     \
# generated text  \
# hello world     \
# """

# text = """
# lorem ipsum     \n\
# generated text \
# hello world \
# """

text = """
lorem ipsum
generated text
hello world
"""

print(text)

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
        # todos = get_todos()
        # todos = get_todos('todos.txt')
        # todos = get_todos(filepath='todos.txt')
        # todos = get_todos('todos1.txt')  # FileNotFoundError
        todos = get_todos()

        todos.append(todo + '\n')

        # save file in txt document
        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()
        # with open('todos.txt', 'w') as file:
        #     file.writelines(todos)
        # write_todos('todos.txt', todos)
        # write_todos('todos.txt', todos)
        # write_todos(filepath='todos.txt', todos_arg=todos)
        write_todos(todos, 'todos.txt')
        # write_todos(todos)

    # elif 'show' in user_action:
    elif user_action.startswith('show'):
        # read files from older docuements - analog system
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # updated system to access file
        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()
        # todos = get_todos()
        # todos = get_todos('todos.txt')
        todos = get_todos()

        print('total items: ', len(todos))

        if len(todos) == 0:
            print('nothing...')
        for index, i in enumerate(todos):
            i = i.strip('\n')
            print(f"{index + 1}.{i}")
            for i in todos:
                i = i.title()

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
            # todos = get_todos()
            # todos = get_todos('todos.txt')
            todos = get_todos()

            existing_todo = todos[number]
            print('older value: ', existing_todo)
            new_todo = input('enter new todo: ')
            print('new value: ', new_todo)

            todos[number] = new_todo + '\n'

            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)
            # write_todos('todos.txt', todos_arg=todos)
            # write_todos(filepath='todos.txt', todos_arg=todos)
            # write_todos(filepath='todos.txt', todos_arg=todos)
            write_todos(todos)

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
            # todos = get_todos()
            # todos = get_todos('todos.txt')
            todos = get_todos()

            index = number - 1
            # if len(todos) > index:
            #     print('item is not found')
            #     # break
            # else:
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)
            # write_todos('todos.txt', todos)
            write_todos(todos)

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
#
#
#
#
#
#
#
