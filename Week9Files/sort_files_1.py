"""
CP1404/CP5632 Practical
Sort Files 1

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""
import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('FilesToSort')
    print("Files are {}".format(os.listdir('.')))
    files = os.listdir('.')  # contains all file names
    file_types = list()

    # find all different file formats
    file_extension = str()
    for file in files:
        for letter in range(-1, -len(file), -1):  # starts searching from the back of file name
            try:
                file[letter - 1]
            except IndexError:
                pass
            else:
                if file[letter] == '.':
                    for index in range(letter + 1, 0):
                        file_extension += file[index]
        file_types.append(file_extension)
        file_extension = ''
    print(file_types)

    # create new directory with file_types
    for file_type in file_types:
        print(file_type)
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass

    # sort the files according to their file type
    source_address = os.getcwd() + '\\'
    destination_address = os.getcwd() + '\\'
    for filename in files:
        current_file_type = str()
        for letter in range(0, len(filename)):
            if filename[letter] == '.':
                for index in range(letter + 1, len(filename)):
                    current_file_type += filename[index]
        source_address += filename
        destination_address += current_file_type
        shutil.move(source_address, destination_address)
        source_address = os.getcwd() + '\\'
        destination_address = os.getcwd() + '\\'


main()
