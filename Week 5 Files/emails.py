"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


def main():
    name_to_email = {}
    input_email = input('Enter email: ')
    # ask user for email
    name_and_email = input_email.split('@')
    name = extract_name(name_and_email[0])
    name = ask_name(name)
    # convert text in front of @ into a name
    # ask user if name is correct
    # if True add into dictionary, else ask for real name and store both



def extract_name(string):
    extracted_name = (' '.join(string.lower().split('.'))).title()
    # Makes every word a lower case letter
    # Splits string with dots as delimiter
    # Joins the array with spaces
    # Makes the first letter of each word into capital letter
    return extracted_name


def ask_name(name):
    while True:
        input_answer = input('Is your name {}? (Y/n)'.format(name))
        if input_answer.lower() == 'n':
            name = input('Enter name: ')
            return name
        elif input_answer.upper == 'Y' or input_answer == '':
            return name
        print('Invalid Input')


