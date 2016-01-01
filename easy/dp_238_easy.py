"""
[2015-10-26] Challenge #238 [Easy] Consonants and Vowels
https://tinyurl.com/rDP-238-easy
"""
# Status: Done

from random import randint

def get_input(message = ""):
    input_string = input("%s>" % message)
    if check_input(input_string) == True:
        return input_string
    else:
        error_message = "Input must contain only letters 'c' and 'v'\n"
        get_input(error_message)

def check_input(input_string):
    for character in input_string:
        if character not in ('c', 'v'):
            return False
    return True
                
def make_word(input_string):
    new_word = []
    
    vowels = 'aeiouy'
    consonants = 'bcdfghjklmnpqrstvwxz'
    
    len_vow = len(vowels)
    len_con = len(consonants)
    
    input_string.lower()
    
    for character in input_string:
        if character == 'c':
            new_word.append(consonants[randint(0, len_con - 1)])
        elif character == 'v':
            new_word.append(vowels[randint(0, len_vow - 1)])
    new_word = ''.join(new_word)
    
    return new_word
    
print(make_word(get_input()))