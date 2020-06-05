"""CP1404/CP5632 Practical -
Car class example.
for Week 8 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name='Car', fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
    """
    def __str__(self):
        return 'Car, Fuel = {}, Odometer = {}'.format(self.fuel, self.odometer)
    """
    """First version for Question 6 on the worksheet"""

    def __str__(self):
        return '{}, Fuel = {}, Odometer = {}'.format(self.name, self.fuel, self.odometer)
