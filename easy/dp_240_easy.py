"""
[2015-11-09] Challenge #240 [Easy] Typoglycemia
https://tinyurl.com/dp-240-easy
"""
# Status: Done 
import random



def shuffler(word_list):
    """Shuffles a list of characters, except for the first and last ones."""
    if len(word_list) < 4:
        return word_list
    else:
        sh_word = word_list[1 : -1]
        random.shuffle(sh_word)
        word_list[1 : -1] = sh_word
        return word_list

def punctuation_handler(word):
    """Shuffles a word. Handles punctuation."""
    word_list = list(word)
    
    not_alpha = dict()
    # reversed() is used to safely delete non-alpha characters
    # from the word_list. 
    for index, element in reversed(list(enumerate(word))):
        if element.isalpha():
            continue
        else:
            not_alpha[index] = element
            del word_list[index]
            
    shuffler(word_list)
    
    for index in sorted(not_alpha):
        word_list.insert(index, not_alpha[index])
    word = ''.join(word_list)
    
    return word


# This file is hidden by the .gitifnore
WORK_FILE = 'dp_240_easy_input.txt'

with open(WORK_FILE, 'r+') as file:
    
    output_lines = str()
    
    for line in file:
        sh_line = list()
        
        for word in line.split(sep = ' '):
            sh_line.append(punctuation_handler(word))
            
        line = ' '.join(sh_line)
        output_lines += line
    
    file.write(output_lines)