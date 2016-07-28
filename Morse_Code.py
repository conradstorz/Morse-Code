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
audio_timing = 60    # milliseconds for a "dot" at 20 words per minute
audio_tone_freq = 750     # standard range is 600-1000 hz
space_tone_freq = 0    # silence

dot_length = 1
dash_length = 3
inter_tone_spacing = 1
word_spacing = 7
letter_spacing = 3

space = ' '
sentence_break = space * 10    # not in the formal definition
word_break = space * word_spacing
letter_break = space * letter_spacing
text_spacing_char = space * 1


def decode_str_representation(morse):
    output = ''


def extract_code(stream):
    output = ''
    last = ' '
    complete = False
    s = list(stream)

    for char in s:
        if char == ' ' and last != ' ':
            return output
        else:
            last = char
            output += char

    return output

            
def clean_whitespace(code):
    output = ''
    s = list(code)
    for char in s:
        if char == ' ':
            output += char
        else:
            break
    if output == '':
        output = code
    return output


def decode(morse):
    output = ''
    if morse == '':
        return output

    sentences = morse.split(sentence_break)

    for sentence in sentences:
        words = sentence.split(word_break)

        for word in words:
            characters = word.split(letter_break)
            print characters
            for character in characters:
                if morse_code_dict.has_key(character.strip()):
                    output += morse_code_dict[character.strip()]
                if character == '':
                    output += ' '
            output += ' '

    return output[:-2]   # strip just the last 2 space characters
    """

    while len(morse) > 0:
        code = extract_code(morse)
        code = clean_whitespace(code)
        if morse_code_dict.has_key(code):
            output += morse_code_dict[code]
        else:
            while len(code) >= 6: #this is one or more spaces
                output += ' '
                code = code[6:] #4 is the length of a space and 3 is the space between characters

        morse = morse[len(code):]

    return output
    """

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

