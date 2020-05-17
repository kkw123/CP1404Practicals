"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

from Week8Files.taxi import Taxi


def main():
    taxi1 = Taxi('Prius 1', 100)
    print(taxi1)
    """First Details"""
    taxi1.drive(40)
    print(taxi1)
    print('Current Fare is: ${}'.format(taxi1.get_fare()))
    """Second Details after 40km driven"""
    taxi1.start_fare()
    taxi1.drive(100)
    print(taxi1)
    print('Current Fare is: ${}'.format(taxi1.get_fare()))
    """Third Details after odo reset and 100km drive"""


main()
