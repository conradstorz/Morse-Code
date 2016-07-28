#!/usr/bin/env python

import sys
import string

morse_code_alphabet = list('0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?/@')

morse_char_dict = {
        'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', 
        
        '.': '.-.-.-', ',': '--..--', '?': '..--..',
        '/': '-..-.', '@': '.--.-.',  ' ': '    ',
        }

# create an inverse dictionary
morse_code_dict = {v: k for k, v in morse_char_dict.items()}

# constants
audio_encode_timing = 60    # milliseconds for a "dot" at 20 words per minute
audio_encode_tone_freq = 750     # standard range is 600-1000 hz
space_tone_freq = 0    # silence

dot_length = 1
dash_length = 3
inter_tone_spacing = 1

sentence_spacing = 10
word_spacing = 7
letter_spacing = 3

space = ' '
sentence_break = space * sentence_spacing    # not in the formal definition
word_break = space * word_spacing
letter_break = space * letter_spacing
text_spacing_char = space * 1


def capture_next_transistion(morse):
    """ pull characters from beginning of string until phase change.
        for example: from silence to sound, or sound to silence. """
    output = ''
    Silence = False
    Code = True
    morse_list = list(morse)

    mode = Silence
    while len(morse_list) > 0:
        char = morse_list.pop(0)

        if char == ' ':
            transmission = Silence
        else:
            transmission = Code

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
    sl = list(string)
    while len(sl) > 0:
        char = sl.pop(0)
        if char != ' ':
            return False
    return True


def equivalent_number_of_space_characters(string):
    output = ''
    chars = ''
    sl = list(string)
    while len(sl) > 0:
        output += sl.pop(0)
        if len(output) == word_spacing:
            chars += ' '
            output = ''
    return chars


def extract_code(stream):
    """ look at stream for identifiable structure. """

    output = capture_next_transistion(stream)

    code = ''
    if morse_code_dict.has_key(output):
        code += morse_code_dict[output]
    else:
        if there_are_only_spaces(output):
            return equivalent_number_of_space_characters(output)
        else:
            return ''
    return code

            
def decode(morse):
    output = ''
    if morse == '':
        return output

    while len(morse) > 0:
        segment = capture_next_transistion(morse)
        morse = morse[len(segment):]
        content = extract_code(segment)
        output += content

    return output


def encode(message):
    output = ''
    for character in message:
        #print character
        #print morse_char_dict[character.upper()]
        if morse_char_dict.has_key(character.upper()):
            output += morse_char_dict[character.upper()]
            output += letter_break
        else:
            output += word_break     # place word break anywhere an unencodeable character exists
    return output

