"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)


def user_input(dict1):
    state_code = input("Enter short state: ")
    while state_code != "":
        if state_code.upper() in dict1:
            print('{} is {}'.format(state_code.upper(), dict1[state_code.upper()]))
        else:
            print("Invalid short state")
        state_code = input("Enter short state: ")


def print_all(dict1):
    for code, name in dict1.items():
        print('{:<3} is {}'.format(code, name))


print_all(CODE_TO_NAME)
