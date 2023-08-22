import zipfile


def extract_archive(archive_paths, destination_dir):
    with zipfile.ZipFile(archive_paths, 'r') as archive:
        archive.extractall(destination_dir)


if __name__ == "__main__":
    extract_archive("compressed.zip", "extracted_files")
