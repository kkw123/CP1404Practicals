"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""
from Week8Files.silver_service_taxi import SilverServiceTaxi


def main():
    car1 = SilverServiceTaxi('Pog', 1000, 2)
    car1.drive(18)
    print(car1.get_fare())


main()