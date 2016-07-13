"""
[2016-07-04] Challenge #274 [Easy] Gold and Treasure: The Beale Cipher
https://tinyurl.com/dp-274-easy
"""
DOE_FILE = r'c:\code\github\rdp\easy\dp_274_easy_doe.txt'
INPUT_FILE = r'c:\code\github\rdp\easy\dp_274_easy_input.txt'
OUTPUT_FILE = r'c:\code\github\rdp\easy\dp_274_easy_output.txt'

with open(DOE_FILE) as file:
    doe_enumerated = dict()
    for line in file.readlines():
        for (i, word) in enumerate(line.split(' '), 1):
            doe_enumerated[i] = word[0]

with open(INPUT_FILE) as file:
    ciphered_list = list(file.read().split(','))
    ciphered_list = [int(n) for n in ciphered_list]

deciphered ="".join([doe_enumerated[n] for n in ciphered_list])
 
if __name__ == '__main__':
    # some problem occurred before word 807
    # doe_enumerated does not reflect necessary character mapping
    # to successfully decipher given message
    print(deciphered)

