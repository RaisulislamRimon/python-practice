while True:
    user_action = input('type add, show, complete, edit or exit: ')

    match user_action:
        case 'add':
            todo = input('type your todo: ') + '\n'
            # read files from older docuements
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            # save file in txt document
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            if len(todos) == 0:
                print('nothing...')

            for index, item in enumerate(todos):
                print(f"{index + 1}.{item}")

            for item in todos:
                item = item.title()
        case 'edit':
            print('Editing...')
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            print(number)
            existing_todo = todos[number]
            print('older value: ', existing_todo)
            new_todo = input('enter new todo: ')
            print('new value: ', new_todo)
            todos[number] = new_todo

        case 'complete':
            number = int(input('number of the todo to complete: '))
            todos.pop(number - 1)

        case 'exit':
            break
        case _:
            print('do not enter random input')

print("bye")


