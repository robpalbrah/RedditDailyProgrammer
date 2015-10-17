# [2015-09-07] Challenge #213 [Easy] Cellular Automata: Rule 90 
# https://www.reddit.com/r/dailyprogrammer/comments/3jz8tt/20150907_challenge_213_easy_cellular_automata/
# Error in the title, 213 instead of 231

# Rule 90 is a Cellular Automata rule based on the XOR function. 

import random

def write_in_file(nextline, work_file):
    """Takes a list, makes it a string and writes it into a file, 
    substituting 1 for 'X' and 0 for whitespace."""
    
    nextline_string = ''.join(nextline) 
    translate_table = {ord('1'): 'X', ord('0'): ' '}
    work_file.write(nextline_string.translate(translate_table) + '\n')

# Random string to see what pattern will emerge     
random_list = [str(random.choice((0, 1))) for i in range(99)]    
random_string = ''.join(random_list)   
input_string = random_string
number_of_lines = 100

work_list = [a for a in input_string] 
work_file = open(r'c:\code\rDP\231_output.txt', 'w')

write_in_file(work_list, work_file)

for n in range(number_of_lines):
    nextline = ['0' for i in range(len(work_list))] 
    index = 0
    
    for elem in work_list:
        # Check if index a boundary element of the list
        if index not in (0, len(work_list) - 1): 
            # (len(work_list) - 1) because indexing starts from 0
            xor_rule = work_list[index - 1] != work_list[index + 1] 
            
            if xor_rule: 
                nextline[index] = '1'
            else:
                nextline[index] = '0'
        index += 1
    work_list = nextline
    
    write_in_file(nextline, work_file)
    
work_file.close()
          
                
                
