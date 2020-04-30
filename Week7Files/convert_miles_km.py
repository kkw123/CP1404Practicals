"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometersApp(App):

    def build(self):
        Window.size = (200, 100)
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self, miles):
        result = miles * 1.6
        self.root.ids.output_value.text = str(result) + 'km'

    def handle_increment(self, number):
        output = int(self.root.ids.input_number.text) + number
        self.root.ids.input_number.text = str(output)


MilesToKilometersApp().run()
