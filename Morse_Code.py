#!/usr/bin/env python

import sys
import string

morse_code_alphabet = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.,?/@')

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
        '/': '-..-.', '@': '.--.-.',
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
letter_spacing = 4

space = ' '
sentence_break = space * 10    # not in the formal definition
word_break = space * 7
letter_break = space * 3
text_spacing_char = space * 2


def decode(morse):
    output = ''
    sentences = morse.split(sentence_break)

    for sentence in sentences:
        words = sentence.strip().split(word_break)

        for word in words:
            characters = word.strip().split(letter_break)

            for character in characters:
                if morse_code_dict.has_key(character.strip()):
                    output += morse_code_dict[character.strip()]
            output += ' '
        #output += '. '
    return output.strip()


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
    return output.strip()

def test_string_to_Morse():
    test_list = [
                ("Sofia", "...   ---   ..-.   ..   .-"),
                ("We the people", ".--   .          -   ....   .          .--.   .   ---   .--.   .-..   ."),
                ("SOPHIA", "...   ---   .--.   ....   ..   .-"),
                ("EUGENIA", ".   ..-   --.   .   -.   ..   .-")]
    for text, code in test_list:
        
        print 'encode: ', text
        encoded = encode(text)
        print encoded
        print len(code), len(encoded)
        assert code == encoded

        print 'decode: ', code
        decoded = decode(code)
        print decoded
        assert decoded == text.upper()

from hypothesis import given, settings
from hypothesis.strategies import text

@given(text(alphabet=morse_code_alphabet))
@settings(max_examples=5000)
def test_encode_eq_decode(st):
    if st == ' ': return
    assert st == decode(encode(st))


if __name__ == '__main__':
    try:
        sample = sys.argv[1]
    except:
        sample = ''
    decoded = decode(sample)
    encoded = encode(sample)
    if decoded != '':
        print decoded
    if encoded != '':
        print encoded
    sys.exit(1)
