from Morse_Code import encode, decode, MORSE_CODE_ALPHABET

def test_string_to_Morse():
    """ test some known examples. """
    test_list = [
        ("Sofia", "...   ---   ..-.   ..   .-   "),
        ("We the people", ".--   .          -   ....   .          .--.   .   ---   .--.   .-..   .   "),
        ("SOPHIA", "...   ---   .--.   ....   ..   .-   "),
        ("EUGENIA", ".   ..-   --.   .   -.   ..   .-   ")
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
def test_encode_eq_decode(st):
    """ Take a string from Hypothesis and encode/decode it. """
    assert st == decode(encode(st))

