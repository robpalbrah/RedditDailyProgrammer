"""
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
"""
import os
import re
import importlib

# Collecting challenge files in one list 
rule = re.compile(r'dp_\d{1,3}_(easy|int|hard).py')
challanges = list()
for three_tuple in os.walk('.'):
    for filename in three_tuple[2]:
        if rule.fullmatch(filename):
            challanges.append(filename)

challanges_difficulty = {'easy': [],
                        'intermediate': [],
                        'hard': []
                        }            
            
for filename in challanges:
    if 'easy' in filename:
        challanges_difficulty['easy'].append(filename)
    elif 'int' in filename:
        challanges_difficulty['intermediate'].append(filename)
    elif 'hard' in filename:
        challanges_difficulty['hard'].append(filename)          

for folder in challanges_difficulty:
    for filename in challanges_difficulty[folder]:
        f = open(r'%s\%s' % (folder, filename), 'r')
        print(folder, filename)
        f.close()
        
class Challange():
    def __init__(self, filename, difficulty):
        self.filename = filename
        self.difficulty = difficulty
        
        self.number = ''.join([character for character in filename 
                               if character.isdigit()])        
        self.work_file = open(r'%s%s' % (difficulty, filename), 'r')


    def get_status(self):
        """Retrieve status (done/unfinished) from the challenge file.
        Unfinished unless explicitly stated otherwise."""
        for line in self.work_file.readline().lower:
            if 'status: done' in line:
                self.status = 'done'
                break
            else:
                self.status = 'unfinished'

    def get_discription(self):
        """Retrieve challenge description."""
        #self.discription = 
        pass

    def get_url(self):
        """Retrieve challenge url."""
        #self.url = 
        pass

class ReadmeFile():
    def __init__(self, file):
        self.file = file
    
    def create(self):
        """Opens README.mk, creates and fills table with challenges."""
        work_file = open(self.file, 'w')
        # Deleting all previous records
        file.seek(0)
        file.trunkate()
    
# Create directory tree for the easy / intermediate / hard directories
# Store directory tree 
# Retrieve and store (or pass) information about the files (challenge
# number, description, status (done / unfinished)
# Initiate a table in README.mk 
# Pass files into respective table cells, create url links 