"""
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
"""
import os
import re
import importlib
import rDP # Reddit Daily Programming repository

# Collecting challenge files in one list 
rule = re.compile(r'dp_\d{1,3}_(easy|int|hard).py')
challanges = list()
for three_tuple in os.walk('.'):
    for filename in three_tuple[2]:
        if rule.fullmatch(filename):
            challanges.append(filename)

class Challange():
    def __init__(self, file)
        self.file = file
        
    def get_number(self):
        """Retrieve challenge number"""
        #self.number = 
        pass

    def get_difficulty(self):
        """Retrieve difficulty (easy/int/hard from the challenge file."""
        #self.difficulty =
        pass
        
    def get_status(self):
        """Retrieve status (done/unfinished) from the challenge file.
        Unfinished unless explicitly stated otherwise."""
        #self.status =
        pass

    def get_discription(self):
        """Retrieve challenge description."""
        #self.discription = 
        pass

    def get_url(self):
        """Retrieve challenge url."""
        #self.url = 
        pass

def make_readme(file_name):
    """Opens README.mk, creates and fills table with challenges."""
    file = open(file_name, 'w')
    # Deleting all previous records
    file.seek(0)
    file.trunkate()
    
# Create directory tree for the easy / intermediate / hard directories
# Store directory tree 
# Retrieve and store (or pass) information about the files (challenge
# number, description, status (done / unfinished)
# Initiate a table in README.mk 
# Pass files into respective table cells, create url links 