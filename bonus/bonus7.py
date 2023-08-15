#
filenames = ["1.doc", "1.report", "1.presentation"]
for filename in filenames:
    # newFileName = filename.title() + ".txt"
    newFileName = filename.replace('.', '-').title() + ".txt"
    filenames = newFileName
    print(filenames)
#




