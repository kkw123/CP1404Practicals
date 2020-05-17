"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

from Week8Files.taxi import Taxi
from Week8Files.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    user_input = str()
    current_vehicle = None
    bill = 0
    print('Let\'s Drive')
    while not user_input.lower() == 'q':
        print('q)uit, c)hoose taxi, d)rive')
        user_input = input('>>> ')
        if user_input.lower() == 'd':
            if current_vehicle is None:
                print('No vehicle chosen')
            else:
                drive_taxi(taxis, current_vehicle, bill)
                bill += taxis[current_vehicle].get_fare()
                """Does drive function on the taxi"""
        elif user_input.lower() == 'c':
            current_vehicle = choose_taxi(taxis, bill)
            """Returns chosen taxi"""
        elif user_input.lower() == 'q':
            break
            """Exits the loop"""
        print('Bill to date: ${:.2f}'.format(bill))
    print('Total Trip Cost: ${:.2f}'.format(bill))
    print('Taxis are now')
    taxi_count = 0
    for taxi in taxis:
        print('{} - {}'.format(taxi_count, taxi))
        taxi_count += 1


def choose_taxi(array, bill):
    print('Taxis Available')
    taxi_count = 0
    for taxi in array:
        print('{} - {}'.format(taxi_count, taxi))
        taxi_count += 1
    choose_input = input('Choose taxi: ')
    return int(choose_input)


def drive_taxi(array, taxi, bill):
    drive_input = int(input('Drive how far? '))
    array[taxi].start_fare()
    array[taxi].drive(drive_input)
    print('Your {} trip cost you ${:.2f}'.format(array[taxi].name, array[taxi].get_fare()))


main()