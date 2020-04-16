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

state_code = input("Enter short state: ")
while state_code != "":
    if state_code.upper() in CODE_TO_NAME:
        print('{:<} is {}'.format(state_code.upper(), CODE_TO_NAME[state_code.upper()]))
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
