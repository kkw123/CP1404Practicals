"""CP1404/CP5632 Practical -
Client code to use the Car class.
"""
# Note that the import has a folder (module) in it.

from Week6Files.car import Car


def main():
    """Demo test code to show how to use car class."""
    """
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    """

    """Create limo Car object"""
    limo = Car('Limo',100)
    """Create limo with 100 fuel"""
    limo.add_fuel(20)
    """Add 20 more units of fuel"""
    print('Fuel =', limo.fuel)
    """Print amount of fuel in limo"""
    limo.drive(115)
    """Attempt to dive 115km"""
    print('Odo =', limo.odometer)
    """Print limo odometer"""
    print(limo)
    """Print Limo details"""




main()