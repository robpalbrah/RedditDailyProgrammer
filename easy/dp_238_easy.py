"""
[2015-10-26] Challenge #238 [Easy] Consonants and Vowels
https://tinyurl.com/rDP-238-easy
"""
# Status: Done

from random import choice

def get_input(message = ""):
    input_string = input("%s>" % message)
    if check_input(input_string) == True:
        return input_string
    else:
        error_message = "Input must contain only letters 'c' and 'v'\n"
        return get_input(error_message)

def check_input(input_string):
    for character in input_string:
        if character not in ('c', 'C', 'v', 'V'):
            return False
    return True
                
def make_word(input_string):
    new_word = []
    alphabet = {'v' :'aeiouy', 'c' : 'bcdfghjklmnpqrstvwxz'}
    alphabet['V'] = alphabet['v'].upper()
    alphabet['C'] = alphabet['c'].upper()
    
    for character in input_string:
        new_word.append(choice(alphabet[character]))
    new_word = ''.join(new_word)
    
    return new_word
if __name__ == '__main__':    
    print(make_word(get_input()))