"""
CP1404/CP5632 Practical
Demos of various os module examples

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('Lyrics/Christmas')
    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    os.mkdir('temp')
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    output = list()
    if len(filename) <= 0:
        output.append('_')
    for index, letter in enumerate(filename):
        try:
            filename[index + 1]
        except IndexError:
            output.append(letter)
        else:
            if letter == ' ':
                output.append('_')
            elif filename[index - 1] == ' ' or filename[index - 1] == '(':
                output.append(letter.upper())
            elif letter.isupper():
                if index == 0:
                    output.append(letter)
                elif filename[index].lower() + filename[index + 1].lower() + filename[index + 2].lower() == 'txt':
                    output.append('txt')
                    break
                elif not filename[index - 1] == ' ':
                    output.append('_')
                    output.append(letter)
            else:
                output.append(letter)
    print(''.join(output))


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


# main()
# demo_walk()
get_fixed_filename('Away In A Manger.txt')
get_fixed_filename('SilentNight.txt')
get_fixed_filename('O little town of bethlehem.TXT')
get_fixed_filename('ItIsWell (oh my soul).txt')
get_fixed_filename('')

