"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

COLOURS = {"aliceblue": "#f0f8ff",
           "aquamarine1": "#7fffd4",
           "blue1": "#0000ff",
           "darkgreen": "#006400",
           "darkorchid": "	#9932cc",
           "darkslateblue": "#483d8b",
           "firebrick": "#b22222",
           "gray1": "#030303",
           "hotpink": "#ff69b4",
           "khaki": "#f0e68c"}


def main():
    user_input = input('Enter a colour: ').strip().lower()
    while not user_input:
        for colour in COLOURS:
            if colour == user_input:
                print(COLOURS.get('user_input'))
        print('Enter a valid colour')
        user_input = input('Enter a colour: ').strip().lower()


main()
