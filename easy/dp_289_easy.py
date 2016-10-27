"""
[2016-10-24] Challenge #289 [Easy] It's super effective!
https://tinyurl.com/dp-289-easy
"""
# Status: Done

INPUT_FILE = 'dp_289_easy_input.txt'

with open(INPUT_FILE) as file:
    file_data = file.readlines()

# list of elements representes as lower case strings 
elements = [element.lower() for element in file_data[0].strip().split()]

# two-dementional array of floating point numbers:
# multipliers[attack_element][defence_element]
multipliers = []
for line in file_data[2:]:
    line = [float(i) for i in line.strip().split()]
    multipliers.append(line)

def damage_multiplier(attack, defence):
    attack_element = elements.index(attack)
    defence_element = elements.index(defence)

    return multipliers[attack_element][defence_element]

print(damage_multiplier('fire', 'grass'))
