"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection=True, year=0):
        """
        Initialise a programming language
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing.lower() == 'dynamic':
            return True
        else:
            return False

    def __str__(self):
        return '{}, {} Typing, Reflection = {}, First appeared in {}'.format(self.name,self.typing,self.reflection,self.year)
