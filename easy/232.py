# Reddit Daily Programming [2015-09-14] Challenge #232 [Easy] Palindromes
# https://www.reddit.com/r/dailyprogrammer/comments/3kx6oh/20150914_challenge_232_easy_palindromes/

lines_number = input("Number of lines: ")

lines = []
for i in range(int(lines_number)):
    input_lines = input('> ')
    lines.append(input_lines.rstrip())
    
print(lines)
    

