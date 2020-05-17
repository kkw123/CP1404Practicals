"""
CP1404/CP5632 Practical
Car class

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""
from Week8Files.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.distance_driven = 0
        self.odometer = 0
        self.reliability = reliability
        """Reliability is the chance for the car will actually drive"""

    def drive(self, distance):
        if randint(1, 100) <= self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return 0





