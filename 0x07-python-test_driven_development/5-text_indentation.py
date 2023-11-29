#!/usr/bin/python3

"""
Note: function with a docstring added to provide a brief description of its purpose and usage
"""

def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'

    Parameters:
    - text (str): The input text to be processed.

    Raises:
    - TypeError: If the input text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    lines = []            # Empty list to store processed lines
    current_line = ''      # Empty string to accumulate characters until a punctuation is encountered

    for char in text:
        current_line += char
        if char in punctuation_chars:
            lines.append(' '.join(line.strip() for line in current_line.split(char) if line.strip()))
            current_line = ''

    if current_line:
        lines.append(' '.join(line.strip() for line in current_line.split(char) if line.strip()))

    print('\n\n'.join(lines))

