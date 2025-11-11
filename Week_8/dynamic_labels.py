from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp( BoxLayout ):
    """BoxLayout subclass that creates labels dynamically from a list of names."""

    def __init__(self, **kwargs):
        """
        Initialize the layout and create labels for each name.
        """
        super().__init__( **kwargs )
        # List of names to display
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
        # Create and add a Label for each name
        for name in self.names:
            label = Label( text=name, size_hint_y=None, height=40 )
            self.add_widget( label )


class MyApp( App ):
    """Application class for running the dynamic labels."""

    def build(self):
        """Builds the main widget."""
        return DynamicLabelsApp()


# Run app
if __name__ == '__main__':
    MyApp().run()