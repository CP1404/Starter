"""
Basic Kivy test code
If this works, it will produce a GUI window with "hello world" in the middle
and you know you have set everything up correctly.
It also prints the Python version in the run output (may be mixed in with Kivy output)
The Python version should be 3.x (not 2.x).
"""

from kivy.app import App
from kivy.uix.button import Button
import sys


class CheckSetupApp(App):

    def build(self):
        return Button(text='hello world')


if __name__ == '__main__':
    # In PyCharm, right-click here and choose 'Run check_setup'
    print("Python version information:", sys.version)
    CheckSetupApp().run()
