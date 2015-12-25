#!/usr/bin/env python

import os
import string

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
        '9': '----.' 
        }

# create an inverse dictionary
morse_code_dict = {v: k for k, v in morse_char_dict.items()}

sentence_break = '       '  #seven spaces
word_break = '   '   #three spaces
letter_break = '  '   #two spaces

def decode(morse):
    output = ''
    sentences = morse.split(sentence_break)
    for sentence in sentences:
        words = sentence.split(word_break)
        for word in words:
            characters = word.split(letter_break)
            for character in characters:
                if morse_code_dict.has_key(character):
                    output += morse_code_dict[character]
            output += ' '
        #output += '. '
    return output


def encode(message):
    output = ''
    for character in message:
        if morse_char_dict.has_key(character.upper()):
            output += morse_char_dict[character.upper()]
            output += letter_break
    return output

def test_string_to_Morse():
    test_list = [
                ("Sofia ", "...  ---  ..-.  ..  .-"),
                ("SOPHIA ", "...  ---  .--.  ....  ..  .-"),
                ("EUGENIA ", ".  ..-  --.  .  -.  ..  .-")]
    for text, code in test_list:
        print 'encode: ', text
        print encode(text)
        print 'decode: ', code
        print decode(code)
        assert decode(code) == text.upper()


if __name__ == '__main__':
    status = decode(sys[0], result)
    if status:
        print result
    sys.exit(status)
