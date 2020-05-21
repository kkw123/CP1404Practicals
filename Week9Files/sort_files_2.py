"""
CP1404/CP5632 Practical
Sort Files 2

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""
import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('FilesToSort2')
    print("Files are {}".format(os.listdir('.')))
    files = os.listdir('.')  # contains all file names
    file_types = dict()

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
        file_types[file_extension] = ''
        file_extension = ''
    print(file_types)

    # Ask the user to categorise different extensions
    for file_type in file_types:
        user_input = input('What category would you like to sort {} files into? '.format(file_type))
        file_types[file_type] = user_input
    print(file_types)

    # file_types = {'doc': 'Docs', 'docx': 'Docs', 'png': 'Images', 'gif': 'Images',
    #               'txt': 'Docs', 'xls': 'Spreadsheets', 'xlsx': 'Spreadsheets', 'jpg': 'Images'}
    # """Sample code to simulate completed user input"""

    # Create a new folder for each unique category
    for file_type, file_category in file_types.items():
        print(file_category)
        try:
            os.mkdir(file_category)
        except FileExistsError:
            pass

    # Transfer files to their folders
    for filename in files:
        source_address = os.getcwd() + '\\'
        destination_address = os.getcwd() + '\\'
        current_file_type = str()
        for letter in range(0, len(filename)):
            if filename[letter] == '.':
                for index in range(letter + 1, len(filename)):
                    current_file_type += filename[index]
        source_address += filename
        destination_address += file_types.get(current_file_type)
        shutil.move(source_address, destination_address)


main()
