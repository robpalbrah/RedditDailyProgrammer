"""
[2016-02-16] Challenge #254 [Easy] Atbash Cipher
https://tinyurl.com/dp-254-easy
"""
# Status: Done

from string import ascii_letters

def atbash_cipher(input_text, decode = False):
    output_text = ''
    for char in input_text:
        if char in ascii_letters:
            char_index = ascii_letters.index(char)

            if decode == True:
                char = ascii_letters[(26 - char_index - 1)]
            else:
                char = ascii_letters[(- char_index - 1 + 26)]

        output_text += char

    return output_text

if __name__ == '__main__':
    challenge_input = ['foobar', 'wizard', '/r/dailyprogrammer',
        'gsrh rh zm vcznkov lu gsv zgyzhs xrksvi']
    test_strings = map(atbash_cipher, challenge_input)
    for text in test_strings:
        print('encoded = ', text)
        print('\tdecoded = ', atbash_cipher(text, decode = True))
        
        
         