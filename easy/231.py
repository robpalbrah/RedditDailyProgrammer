# [2015-09-07] Challenge #213 [Easy] Cellular Automata: Rule 90 
# https://www.reddit.com/r/dailyprogrammer/comments/3jz8tt/20150907_challenge_213_easy_cellular_automata/
# Error in the title, 213 instead of 231

# Rule 90 is a Cellular Automata rule based on the XOR function. 

input_string = input('> ')

number_of_lines = 25 

work_list = [a for a in input_string] 

for n in range(number_of_lines):
    nextline = ['0' for i in range(len(work_list))] 
    for elem in work_list:
        index = work_list.index(elem)
        xor_rule = work_list[index - 1] != work_list[index + 1] 
        # Check if index a boundary element of the list
        if index not in (0, len(work_list)):
            if xor_rule: 
                nextline[index] = '1'
            else:
                nextline[index] = '0'
                
    work_list = nextline
    
    nextline_string = ''.join(nextline)
    nextline_string.translate({ord('1'): 'X'})
    print(nextline_string)
                
                
                
