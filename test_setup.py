"""
Basic Kivy test code
If this works, it will produce a GUI window with "hello world" in the middle
and you know you have set everything up correctly
"""

from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):

    def build(self):
        return Button(text='hello world')

TestApp().run()

