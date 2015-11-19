"""
[2015-06-01] Challenge #217 [Easy] Lumberjack Pile Problem
https://tinyurl.com/dp-217-easy
"""
# Status: Done

file = open('dp_217_easy_input.txt', 'r')

input = [int(n) for n in file.read().split()]

grid_size = input[0]
logs_number = input[1]
lumber_piles = input[2:]

smallest_pile = min(lumber_piles)

while logs_number > 0:
    for index, pile in enumerate(lumber_piles):
        if logs_number <= 0:
            break 
        if pile == smallest_pile:
                logs_number -= 1
                lumber_piles[index] += 1
    smallest_pile += 1
  
for index, pile in enumerate(lumber_piles, 1):
    if index % grid_size == 0:
        print_ends = '\n'
    else:
        print_ends = ' '
        
    print(pile, end = print_ends)