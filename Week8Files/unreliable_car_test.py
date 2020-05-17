"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

from Week8Files.UnreliableCar import UnreliableCar


def main():
    car1 = UnreliableCar('Not Good Car', 1000, 20)
    """Car has 20% chance to drive properly"""
    print(car1)
    while car1.fuel > 500:
        car1.drive(100)
        print(car1)
    """Test if the car does have a chance to fail the drive function"""


main()
