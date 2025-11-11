"""
CP1404/CP5632 Practical - Suggested Solution

GUI program to convert miles to kilometres

Lindsay Ward, IT@JCU

Print statements included to see when the functions run.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

FACTOR_MILES_TO_KM = 1.60934


class MilesConverterApp( App ):
    """Kivy App for converting miles to kilometres."""

    output_km = StringProperty()

    def build(self):
        """Build the app and load kv layout."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file( 'convert_miles_km.kv' )
        return self.root

    def handle_calculate(self, text):
        """
        Handle calculation of miles to km when button is pressed.

        Args:
            text (str): The input miles as string.
        """
        print( "handle calculate" )
        miles = self.convert_to_number( text )
        self.update_result( miles )

    def handle_increment(self, text, change):
        """
        Handle increment/decrement button press.

        Args:
            text (str): Current miles input as string.
            change (float): Increment or decrement value.
        """
        print( "handle increment" )
        miles = self.convert_to_number( text ) + change
        self.root.ids.input_miles.text = str( miles )

    def update_result(self, miles):
        """
        Update the output property with the km conversion.

        Args:
            miles (float): The miles value to convert.
        """
        print( "update" )
        self.output_km = str( miles * FACTOR_MILES_TO_KM )

    @staticmethod
    def convert_to_number(text):
        """
        Convert string to float; return 0.0 if invalid.

        Args:
            text (str): The input string.

        Returns:
            float: Converted number or 0.0 if error.
        """
        try:
            return float( text )
        except ValueError:
            return 0.0


# Run app
if __name__ == '__main__':
    MilesConverterApp().run()