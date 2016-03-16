"""
[2016-03-07] Challenge #257 [Easy] In what year were most presidents alive?
https://tinyurl.com/dp-257-easy
"""
# Status: Done
import csv
from datetime import date
from itertools import islice


INPUT_FILE = "dp_257_easy_input.csv"

# Lists to hold birth and death years
years_birth = list()
years_death = list()

# Taking values from the .csv file
with open(INPUT_FILE, newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in islice(reader, 1, None):
        # 2nd column contains birth dates in 'day month year' format
        birth_year = row[1].strip().split(' ')[2]
        years_birth.append(int(birth_year))
        
        # 4th column contains death dates in the same format
        # Some presidents might still be alive 
        try:
            death_year = row[3].strip().split(' ')[2]
            years_death.append(int(death_year))
        except IndexError: pass

# sorting birth and death years 
years_birth = sorted(years_birth)
years_death = sorted(years_death)

min_year = min(min(years_birth), min(years_death))
max_year = date.today().year

# sentinels 
years_birth.append(float('inf'))
years_death.append(float('inf'))

num_alive = 0
max_alive = 0


# counters 
i = 0           # for years_birth
k = 0           # for years_death

for year in range(min_year, max_year):
    
    while year == years_birth[i]:
        num_alive += 1
        i += 1
        if num_alive > max_alive:
            max_alive = num_alive
            years_most_alive = list()        
    
    if max_alive == num_alive:
        years_most_alive.append(year)
    
    while year == years_death[k]:
        num_alive -= 1
        k += 1

print(years_most_alive)
        
    




