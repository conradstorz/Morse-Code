#!/usr/bin/env python

import string

letters = [('A',".-"),   ('B',"-..."), ('C',"-.-."), ('D',"-.."), ('E',"."),
           ('F',"..-."), ('G',"--."),  ('H',"...."), ('I',".."),  ('J',".---"),
           ('K',"-.-"),  ('L',".-.."), ('M',"--"),   ('N',"-."),  ('O',"---"),
           ('P',".--."), ('Q',"--.-"), ('R',".-."),  ('S',"..."), ('T',"-"),
           ('U',"..-"),  ('V',"...-"), ('W',".--"),  ('X',"-..-"),('Y',"-.--"),
           ('Z',"--..")]

def decode(input):
    if input == "" :
        return [""]
    else:
        return [ letter + remaining
                 for letter, code in letters if input.startswith(code)
                 for remaining in decode(input[len(code):]) ]

# Some Testing code
def test(s, code):
    if s in decode(code):
        print code + " can be decoded as " + s
    else:
        print code + " can NOT be decoded as " + s

test("SOFIA", "...---..-....-")
test("SOPHIA", "...---..-....-")
test("EUGENIA", "...---..-....-")
