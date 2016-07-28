import sys
import Morse_Code

if __name__ == '__main__':

    try:
        # look for string on command line
        sample = sys.argv[1]
    except:
        # if no command, print usage instructions
        print 'Morse.py: USAGE; Morse.py "string to be encoded/decoded"'
        sys.exit(1)

    decoded = Morse_Code.decode(sample)
    encoded = Morse_Code.encode(sample)
    if decoded != '':
        print 'Original string decodes to: "{}"'.format(decoded)
    if encoded != '':
        print 'Original string encodes to: "{}"'.format(encoded)
    print 'Original string: "{}"'.format(sample)
    sys.exit(0)
