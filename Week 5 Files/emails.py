"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


def main():
    names_to_emails = {}
    input_email = input('Enter email: ')
    # ask user for email
    while input_email != '':
        name_and_email = input_email.split('@')
        name = extract_name(name_and_email[0])
        # convert text in front of @ into a name
        name = ask_name(name)
        # ask user if name is correct
        names_to_emails[name] = input_email
        # if True add into dictionary, else ask for real name and store both
        input_email = input('Enter email: ')
    print_results(names_to_emails)


def extract_name(string):
    extracted_name = (' '.join(string.lower().split('.'))).title()
    # Makes every word a lower case letter
    # Splits string with dots as delimiter
    # Joins the array with spaces
    # Makes the first letter of each word into capital letter
    return extracted_name


def ask_name(name):
    while True:
        input_answer = input('Is your name {}? (Y/n) '.format(name))
        if input_answer.lower() == 'n' or input_answer.lower() == 'no':
            name = input('Enter name: ')
            return name
        elif input_answer.upper() == 'Y' or input_answer == '':
            return name
        print('Invalid Input')


def print_results(dict1):
    for name, email in dict1.items():
        print('{} ({})'.format(name, email))
main()
