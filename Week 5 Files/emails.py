"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


def main():
    input_email = input('Enter email: ')
    # ask user for email
    name_and_email = input_email.split('@')
    name = extract_name(name_and_email[0])
    # convert text in front of @ into a name
    # ask user if name is correct
    # if True add into dictionary, else ask for real name and store both
    pass


def extract_name(string):
    extracted_name = (' '.join(string.lower().split('.'))).title()
    print(extracted_name)


extract_name('linDsay.wArd')


