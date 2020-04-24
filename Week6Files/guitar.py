"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        return 2020 - self.year

    def is_vintage(self):
        return self.get_age() >= 50

    def __str__(self):
        return '{} ({}) : ${:,}'.format(self.name, self.year, self.cost)
