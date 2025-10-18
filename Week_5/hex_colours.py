"""
File: hex_colours.py
Description:
Allows the user to lookup hexadecimal colour codes by name.
Colour names are case-independent.
User can enter colour names repeatedly; blank input ends the program.
"""

# Constant dictionary of 10 colour names and their hex codes
COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "black": "#000000",
    "cyan": "#00ffff",
    "darkorange": "#ff8c00",
    "goldenrod": "#daa520",
    "lavender": "#e6e6fa",
    "maroon": "#800000",
    "navy": "#000080",
    "olive": "#808000",
    "salmon": "#fa8072"
}


def main():
    while True:
        colour_name = input( "Enter colour name (blank to quit): " ).strip().lower()
        if not colour_name:  # Exit if input is blank
            print( "Goodbye!" )
            break
        hex_code = COLOUR_CODES.get( colour_name )
        if hex_code:
            print( f"The hex code for {colour_name} is {hex_code}" )
        else:
            print( f"Colour '{colour_name}' not found. Please try again." )


if __name__ == "__main__":
    main()
