import sys
from Morse_Code import decode, encode

if __name__ == '__main__':

    try:
        # look for string on command line
        SAMPLE = sys.argv[1]
    except:
        # if no command, print usage instructions
        print 'Morse.py: USAGE; Morse.py "string to be encoded/decoded"'
        sys.exit(1)

    DECODED = decode(SAMPLE)
    ENCODED = encode(SAMPLE)
    if DECODED != '':
        print 'Original string decodes to: "{}"'.format(DECODED)
    if ENCODED != '':
        print 'Original string encodes to: "{}"'.format(ENCODED)
        print 'and decodes to: "{}"'.format(decode(ENCODED))
    print 'Original string: "{}"'.format(SAMPLE)
    sys.exit(0)
