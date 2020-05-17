"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

from Week8Files.taxi import Taxi
from Week8Files.SilverServiceTaxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    user_input = str()
    while not user_input.lower() == 'q':
        print('Let\'s Drive')
        print('q)uit, c)hoose taxi, d)rive')
        user_input = input('>>> ')
        if user_input.lower() == 'q':
            pass
        elif user_input.lower() == 'c':
            pass
        elif user_input.lower() == 'q':
            pass
        else:
            print('Wrong Input')


main()