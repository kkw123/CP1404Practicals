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
    current_vehicle = None
    while not user_input.lower() == 'q':
        print('Let\'s Drive')
        print('q)uit, c)hoose taxi, d)rive')
        user_input = input('>>> ')
        if user_input.lower() == 'd':
            if current_vehicle is None:
                print('No vehicle chosen')
            else:
                pass
            """Does drive function on the taxi"""
        elif user_input.lower() == 'c':
            current_vehicle = choose_taxi(taxis)
            """Returns chosen taxi"""
        elif user_input.lower() == 'q':
            pass
            """Exits the loop"""


def choose_taxi(array):
    """Only breaks if valid Taxi chosen"""
    print('Taxis Available')
    taxi_count = 0
    for taxi in array:
        print('{} - {}'.format(taxi_count, taxi))
        taxi_count += 1
    choose_input = input('Choose taxi: ')
    return choose_input


main()