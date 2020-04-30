"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometersApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        Window.size = (200, 100)
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesToKilometersApp.run()
