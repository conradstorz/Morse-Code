#!/usr/bin/env python

import sys
import string

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
AUDIO_ENCODE_TIMING = 60    # milliseconds for a "dot" at 20 words per minute
AUDIO_ENCODE_TONE_FREQ = 750     # standard range is 600-1000 hz
SPACE_TONE_FREQ = 0    # silence

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


def there_are_only_SPACEs(string):
    """ Check string for any character that is not a space. """
    sl = list(string)
    while len(sl) > 0:
        char = sl.pop(0)
        if char != ' ':
            return False
    return True


def equivalent_number_of_SPACE_characters(string):
    """ Given string of spaces return one space character for each seven spaces. """
    output = ''
    chars = ''
    sl = list(string)
    while len(sl) > 0:
        output += sl.pop(0)
        if len(output) == WORD_SPACING:
            chars += ' '
            output = ''
    return chars


def extract_code(stream):
    """ look at stream for identifiable structure. """

    output = capture_next_transistion(stream)

    code = ''
    if MORSE_CODE_DICT.has_key(output):
        code += MORSE_CODE_DICT[output]
    else:
        if there_are_only_SPACEs(output):
            return equivalent_number_of_SPACE_characters(output)
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
        if MORSE_CHAR_DICT.has_key(character.upper()):
            output += MORSE_CHAR_DICT[character.upper()]
            output += LETTER_BREAK
        else:
            # place word break anywhere an unencodeable character exists
            output += WORD_BREAK
    return output

