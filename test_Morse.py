""" Test code """

from Morse_Code import encode, decode, MORSE_CODE_ALPHABET, MORSE_CHAR_DICT


def test_given_alphabet_has_code_for_each_character():
    """ Verify that all valid characters have a code assigned to them and that all codes are unique.
        """
    codes = set()
    for char in MORSE_CODE_ALPHABET:
        assert MORSE_CHAR_DICT.has_key(char)
        codes.add(MORSE_CHAR_DICT[char])
    assert len(codes) == len(MORSE_CODE_ALPHABET)


def test_string_to_morse():
    """ test some known examples. """
    test_list = [
        ("Sofia", "...   ---   ..-.   ..   .-   "),
        ("We the people", ".--   .          -   ....   .          .--.   .   ---   .--.   .-..   .   "),
        ("SOPHIA", "...   ---   .--.   ....   ..   .-   "),
        ("EUGENIA", ".   ..-   --.   .   -.   ..   .-   "),
        ]

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

@given(text(alphabet=MORSE_CODE_ALPHABET))
@settings(max_examples=5000)
def test_encode_eq_decode(string):
    """ Take a string from Hypothesis and encode/decode it. """
    assert string == decode(encode(string))

