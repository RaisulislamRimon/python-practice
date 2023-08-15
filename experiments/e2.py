# while True:
#     print('hello')
todos = []
while True:
    todo = input('enter :')
    print(todo.capitalize())
    print(todo.title) #  <built-in method title of str object at 0x0000000853D56D80>
    print(todo.title())
    todos.append(todo)
    print(todos)


