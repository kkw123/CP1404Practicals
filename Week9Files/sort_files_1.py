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
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    for a in os.walk('.'):
        print(a)

main()