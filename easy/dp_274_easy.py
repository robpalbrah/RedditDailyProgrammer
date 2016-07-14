"""
[2016-07-04] Challenge #274 [Easy] Gold and Treasure: The Beale Cipher
https://tinyurl.com/dp-274-easy
"""
# Status: Done

import random

DOE_FILE = r'c:\code\github\rdp\easy\dp_274_easy_doe.txt'
INPUT_FILE = r'c:\code\github\rdp\easy\dp_274_easy_input.txt'

with open(DOE_FILE) as file:
    doe_enumerated = list()
    for line in file.readlines():
        for word in line.split(' '):
            doe_enumerated.append(word[0])

with open(INPUT_FILE) as file:
    ciphered_list = list(file.read().split(','))
    ciphered_list = [int(n) for n in ciphered_list]

deciphered ="".join([doe_enumerated[n-1] for n in ciphered_list])

if __name__ == '__main__':
    # some problem occurred before word 647
    # doe_enumerated does not reflect necessary character mapping
    # to successfully decipher given message
    print(deciphered)
