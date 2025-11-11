from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutDemo( BoxLayout ):
    """BoxLayout with greeting and clear functions."""

    def handle_greet(self):
        """
        Update label with greeting including the entered name.
        """
        self.ids.output_label.text = f"Hello {self.ids.input_name.text}"

    def handle_clear(self):
        """
        Clear the input and output labels.
        """
        self.ids.input_name.text = ''
        self.ids.output_label.text = ''


class MyApp( App ):
    """Application class for BoxLayoutDemo."""

    def build(self):
        """Build and return the root layout."""
        return BoxLayoutDemo()


# Run app
if __name__ == '__main__':
    MyApp().run()