import zipfile
import pathlib

message = 'Successful'


def make_archive(filepaths, destination_dir):
    destination_path = pathlib.Path(destination_dir, 'compressed.zip')
    with zipfile.ZipFile(destination_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
        return message


if __name__ == "__main__":
    print('__name__ == __main__')
    make_archive(filepaths=['bonus1.py', 'bonus2.py'],
                 destination_dir='zipped dir')
