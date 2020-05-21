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
                    for array in range(letter + 1, 0):
                        file_extension += file[array]
        file_types.append(file_extension)
        file_extension = ''
    print(file_types)

    # create new directory with file_types


main()