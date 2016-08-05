#!/usr/bin/env python
""" Functions for encoding/decoding strings to/from Morse Code representation.
    """

MORSE_CODE_ALPHABET = list(
    """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?/@ :'-("="""
    )

MORSE_CHAR_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
    ',': '--..--', '?': '..--..', '/': '-..-.', '@': '.--.-.', ' ': '    ',
    ':': '---...', "'": '.----.', '-': '-....-', '(': '-.--.-',
    '"': '.-..-.', '=': '-...-',
    }

# create an inverse dictionary
MORSE_CODE_DICT = {v: k for k, v in MORSE_CHAR_DICT.items()}

# constants
AUDIO_ENCODE_TIMING = 60         # milliseconds for a "dot"
                                 # at 20 words per minute.
AUDIO_ENCODE_TONE_FREQ = 750     # standard range is 600-1000 hz
SPACE_TONE_FREQ = 0              # silence

DOT_LENGTH = 1
DASH_LENGTH = 3
INTER_TONE_SPACING = 1

SENTENCE_SPACING = 10
WORD_SPACING = 7
LETTER_SPACING = 3

SPACE = ' '
SENTENCE_BREAK = SPACE * SENTENCE_SPACING    # not in the formal definition
WORD_BREAK = SPACE * WORD_SPACING
LETTER_BREAK = SPACE * LETTER_SPACING
TEXT_SPACING_CHAR = SPACE * 1


def split_string_on_edges(morse):
    """ return a list of substrings that represent all the elements of
        the presented string. Morse code is represented as a pattern of
        sounds seperated by measured silences. A string representation
        of Morse is composed of silence represented by the use of
        a space character {' '} and sounds represented by
        dots and dashes {'.' and '-'}. This function will break a string
        on whitespace and place each group of silences
        and sounds into seperate stings in a list.
        """


#@given() # allow Hypothesis to send any input
def test_split_string_on_edges_operation(test_input):
    """ SSOE should return a list of strings.
        SSOE returned list should contain ALL parts of the orginal string.
        Returned list should be alternating strings of whitespace and text.
        Any input to SSOE that is not a string should return an empty list.
        """


def capture_next_transistion(morse):
    """ pull characters from beginning of string until phase change.
        for example: from silence to sound, or sound to silence. """
    output = ''
    SILENCE = False
    CODE = True
    morse_list = list(morse)

    mode = SILENCE
    while len(morse_list) > 0:
        char = morse_list.pop(0)

        if char == ' ':
            transmission = SILENCE
        else:
            transmission = CODE

        if output == '':
            output += char
            mode = transmission
        else:
            if mode == transmission:
                output += char
            else:
                return output
    return output


def there_are_only_spaces(string):
    """ Check string for any character that is not a space. """
    slist = list(string)
    while len(slist) > 0:
        char = slist.pop(0)
        if char != ' ':
            return False
    return True


def equivalent_number_of_space_characters(string):
    """ Given string of spaces return one space character
        for each seven spaces.
        """
    output = ''
    chars = ''
    slist = list(string)
    while len(slist) > 0:
        output += slist.pop(0)
        if len(output) == WORD_SPACING:
            chars += ' '
            output = ''
    return chars


def extract_code(stream):
    """ look at stream for identifiable structure. """

    output = capture_next_transistion(stream)

    code = ''
    if output in MORSE_CODE_DICT:
        code += MORSE_CODE_DICT[output]
    else:
        if there_are_only_spaces(output):
            return equivalent_number_of_space_characters(output)
        else:
            return ''
    return code


def decode(morse):
    """ Turn a string of dots and dashes into alphanumeric text. """
    output = ''
    if morse != '':
        while len(morse) > 0:
            segment = capture_next_transistion(morse)
            morse = morse[len(segment):]
            content = extract_code(segment)
            output += content
    return output


def encode(message):
    """ Convert a string of text into a string of dots and dashes. """
    output = ''
    for character in message:
        if character.upper() in MORSE_CHAR_DICT:
            output += MORSE_CHAR_DICT[character.upper()]
            output += LETTER_BREAK
        else:
            # place word break anywhere an unencodeable character exists
            output += WORD_BREAK
    return output
