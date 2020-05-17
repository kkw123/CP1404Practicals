"""
CP1404/CP5632 Practical
Car class

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""
from Week8Files.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), SilverServiceTaxi.flagfall)

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance + SilverServiceTaxi.flagfall




