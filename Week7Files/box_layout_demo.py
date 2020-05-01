"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


from kivy.app import App
from kivy.lang import Builder

"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_input(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Hello '


BoxLayoutDemo().run()
