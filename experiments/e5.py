import glob

# myfiles = glob.glob('files/*.txt')
# myfiles = glob.glob('files/*.txt')
# myfiles = glob.glob('*.txt')
# myfiles = glob.glob('*')
myfiles = glob.glob('files/*')

for filepath in myfiles:
    with open(filepath, 'r') as file:
        # print(file.readlines())
        # print(file.read())
        print(file.read().upper())

# print(myfiles)
# print('total files:', len(myfiles))
