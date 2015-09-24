# Reddit Daily Programming [2015-09-14] Challenge #232 [Easy] Palindromes
# https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/

lines_number = input("Number of lines: ")

lines = []
for i in range(int(lines_number)):
    input_lines = input('> ').lower()
    input_lines = input_lines.translate({ord(i): None for i in ' $&?.,#!;:-'})
    lines.append(input_lines.rstrip())
    
lines = ''.join(lines)
lines_reversed = lines[::-1] 

if lines == lines_reversed:
    print('Palindrome')
else:
    print('Not a palindrome')

    

