try:
    width = float(input('Enter rectangle width: '))
    length = float(input('Enter rectangle length: '))

    if width == length:
        # print("That looks like a square")
        exit("That looks like a square")

    area = width * length
    print(area)
except ValueError:
    print('input should be numbers only')



















