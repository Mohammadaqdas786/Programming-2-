"""
CP1404/CP5632 Practical

Kivy GUI program to square a number

Lindsay Ward, IT@JCU
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp( App ):
    """Kivy App for squaring a number."""

    def build(self):
        """Set window size, title, and load the kv file."""
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file( 'squaring.kv' )
        return self.root

    def handle_calculate(self, value):
        """
        Handle the button press to square the input value and display the result.

        Args:
            value (str): The input string to be squared.
        """
        try:
            result = int( value ) ** 2
            self.root.ids.output_label.text = str( result )
        except ValueError:
            self.root.ids.output_label.text = ""


# Run app
if __name__ == '__main__':
    SquareNumberApp().run()