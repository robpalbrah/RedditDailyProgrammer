# Reddit Daily Programming [2015-09-14] Challenge #232 [Easy] Palindromes
# https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/

file = open(r'C:\code\rDP\DemetriMartin.txt', 'r')

lines = []
for file_line in file.readlines():
    
    table_string = u'\u2026\u201C\u201D\u2019 "$&?.,#!;:-()\'\"'
    tr_table = {ord(i): None for i in table_string} 
    
    input_lines = file_line.lower().translate(tr_table)
    
    lines.append(input_lines.rstrip())

file.close()
    
lines = ''.join(lines)
lines_reversed = lines[::-1] 

if lines == lines_reversed:
    print('Palindrome')
else:
    print('Not a palindrome')