import re
from PIL import Image, ImageDraw, ImageFont

def render_ansi_text_to_image(text_lines, filename='my_colored_text.png'):
    # Define the ANSI color codes with both \033 and \x1b variations
    color_codes = {
        '\033[91m': (255, 0, 0), '\x1b[91m': (255, 0, 0),    # Red
        '\033[92m': (0, 255, 0), '\x1b[92m': (0, 255, 0),    # Green
        '\033[93m': (255, 255, 0), '\x1b[93m': (255, 255, 0),# Yellow
        '\033[94m': (0, 0, 255), '\x1b[94m': (0, 0, 255),    # Blue
        '\033[95m': (255, 0, 255), '\x1b[95m': (255, 0, 255),# Magenta
        '\033[96m': (0, 255, 255), '\x1b[96m': (0, 255, 255),# Cyan
        '\033[97m': (255, 255, 255), '\x1b[97m': (255, 255, 255) # White
    }
    reset_code = '\033[0m'  # Reset color code (commonly used)

    # Create an image with a black background
    width, height = 1280, 10 + 15 * len(text_lines)
    image = Image.new('RGB', (width, height), "black")
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    x, y = 10, 10
    line_height = 15

    # Process each line (list of strings) and render it with its respective color
    for line in text_lines:
        for segment in line:
            # Attempt to find the color code at the beginning of the segment
            for code, code_color in color_codes.items():
                if segment[:len(code)] == code:  # Directly compare the beginning of the segment with the color code
                    color = code_color
                    char = segment[len(code):len(code)+1]  # Assume the character is right after the code
                    draw.text((x, y), char, font=font, fill=color)
                    x += font.getsize(char)[0]  # Move x to the end of the last character
                    break
        x = 10  # Reset x to the start of the line for the next line
        y += line_height  # Move to the next line
    imagebox = image.getbbox()
    cropped = image.crop(imagebox)
    # Save the image
    cropped.save(filename)

# Example usage:
text_lines = [
    ['\033[94m-\033[0m', '\033[92m+\033[0m'],
    ['\033[93m@\033[0m', '\033[91m#\033[0m'],
    # ... more lines as needed ...
]

# Call the function with the list of colored text lines and the desired filename
render_ansi_text_to_image(text_lines)


# ANSI escape codes for some colors
RED_AOCTOOLS = '\033[91m'
GREEN_AOCTOOLS = '\033[92m'
YELLOW_AOCTOOLS = '\033[93m'
BLUE_AOCTOOLS = '\033[94m'
MAGENTA_AOCTOOLS = '\033[95m'
CYAN_AOCTOOLS = '\033[96m'
WHITE_AOCTOOLS = '\033[97m'
RESET_AOCTOOLS = '\033[0m'  # Resets the color to default

"""
# Example usage
print(RED + "This is red text." + RESET)
print(GREEN + "This is green text." + RESET)
print(YELLOW + "This is yellow text." + RESET)
"""

def length_without_ansi(s):
    # Regular expression to match ANSI escape codes
    ansi_escape = re.compile(r'\x1b\[([0-9A-Za-z;]*m)')
    # Remove the ANSI escape codes
    cleaned_string = ansi_escape.sub('', s)
    # Return the length of the string without ANSI codes
    return len(cleaned_string)

def print_with_padding(element, max_width):
    # Calculate the length of the ANSI escape codes
    ansi_escape_codes_length = len('\x1b[92m') + len('\x1b[0m')

    # Adjust max_width to account for the non-visible characters of the ANSI codes
    adjusted_width = max_width + ansi_escape_codes_length

    # Print the element with the adjusted width
    print(f"{element:>{adjusted_width}}", end=" ")

def print_2darrays_side_by_side(array1, array2, a1_has_ansi=False, a2_has_ansi=False):
    """ Takes 2 arrays and displays them. It's good for spacing"""
    # Find the maximum width of any number in array2 for proper spacing
    max_width = max(
            length_without_ansi(str(element))
            for array in (array1, array2)
            for row in array
            for element in row)
        
    # Determine the number of rows and columns
    num_rows = len(array1)
    num_columns = len(array1[0])

    # Print column indices
    print("".join(f"_"*len(str(num_rows))), "_".join(f"{i:>{max_width}}" for _ in range(2) for i in range(num_columns)))

    # Print each row with row indices
    for i in range(num_rows):
        # Print row index for array 1
        print(f'{i:{len(str(num_rows))}}:',end="")
        # Print array1 elements
        for element in array1[i]:
            if a1_has_ansi:
                print_with_padding(element,max_width)
            else:
                print(f"{element:>{max_width}}", end=" ")
        for element in array2[i]:
            if a2_has_ansi:
                print_with_padding(element,max_width)
            else: 
                print(f"{element:>{max_width}}", end=" ")
        print()

"""array1 = [['a', 'b', 'c'], ['d', 'e', 'f']]
array2 = [[123, 45, 6], [78900000, 12, 345]]

print_2darrays_side_by_side(array1, array2)"""
