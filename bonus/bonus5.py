# organizing text documents in different files

contents = ['Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
            'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.',
            'Contrary to popular belief, Lorem Ipsum is not simply random text. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which do not look even slightly believable.'
            ]
fileNames = ['doc.txt', 'resport.txt', 'presentation.txt']

# for content, filename in zip(contents, fileNames):
#     file = open(f"folders/{filename}", 'w')
#     file.write(content)
#


for content, filename in zip(contents, fileNames):
    file = open(f"folders/{filename}", 'w')
    file.write(content)



























