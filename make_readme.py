"""
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
"""
import os
import re

class Challenge():
    def __init__(self, filename, difficulty):
        self.filename = filename
        self.difficulty = difficulty

        self.number = ''.join([character for character in filename
                               if character.isdigit()])

    def open_file(self):
        self.work_file = open(r'%s\%s' % (self.difficulty, self.filename), 'r')

    def close_file(self):
        self.work_file.close()

    def get_status(self):
        """Retrieve status (done/unfinished) from the challenge file.
        Unfinished unless explicitly stated otherwise."""
        self.work_file.seek(0)
        for line in self.work_file:
            if 'done' in line.lower():
                self.status = 'done'
                break
            else:
                self.status = 'unfinished'

    def get_discription(self):
        """Retrieve challenge description."""
        self.work_file.seek(0)
        self.discription = self.work_file.readlines()[1]
        self.discription = self.discription[self.discription.rfind(']') + 1:]
        self.discription = self.discription.lstrip().rstrip()

    def get_url(self):
        """Retrieve challenge url."""
        self.work_file.seek(0)
        self.url = self.work_file.readlines()[2].lstrip().rstrip()

def collect_files():
    """Collects challenge files in one dictionary in
    {difficulty:[file1, file2, ...} format."""
    # RegEx rule requires challenge files to be named
    # dp_number_difficulty.py
    rule = re.compile(r'dp_\d{1,3}_(easy|int|hard).py')
    challenges = list()

    for three_tuple in os.walk('.'):
        for filename in three_tuple[2]:
            if rule.fullmatch(filename):
                challenges.append(filename)

    challenges_difficulty = {'easy': [],
                            'intermediate': [],
                            'hard': []
                            }

    for filename in challenges:
        if 'easy' in filename:
            challenges_difficulty['easy'].append(filename)
        elif 'int' in filename:
            challenges_difficulty['intermediate'].append(filename)
        elif 'hard' in filename:
            challenges_difficulty['hard'].append(filename)

    return challenges_difficulty

def create_table(challenges_difficulty):
    """Creates challanges_numbers dictionary
    {number:[easy, intermediate, hard], ...}"""

    numbers = set()
    for challenges_list in challenges_difficulty.values():
        for filename in challenges_list:
            challenge_number = int(''.join([character for character
                                        in filename if character.isdigit()]))
            numbers.add(challenge_number)

    challenges_table = {number: ['---'] * 3 for number in range(
                                    min(numbers), max(numbers) + 1)}

    difficulty_levels = ('easy', 'intermediate', 'hard')

    for index, difficulty in enumerate(difficulty_levels):
        for filename in challenges_difficulty[difficulty]:
            number = int(''.join([character for character
                                        in filename if character.isdigit()]))
            challenges_table[number][index] = filename

    return challenges_table

def fill_cell(status, url, description):
    return '[%s](%s "%s")' % (status, url, description)

def fill_table(challenges_table):
    """Fills dictionary in {number:[easy, intermediate, hard], ...} format.
    If no challenge file for this combination of number/difficulty
    string '---' will be put on it's place. Every existent item will
    be filled in fallowing format: [status](url "description")"""
    difficulty_levels = ('easy', 'int', 'hard')

    for number in challenges_table:
        for filename in challenges_table[number]:
            if filename != "---":
                index = challenges_table[number].index(filename)
                difficulty = difficulty_levels[index]
                # Initiating instance of a class Challenge
                challenge = Challenge(filename, difficulty)

                challenge.open_file()
                challenge.get_status()
                challenge.get_discription()
                challenge.get_url()

                challenges_table[number][index] = fill_cell(
                    challenge.status, challenge.url, challenge.discription)

                challenge.close_file()

    return challenges_table

def create_readme(challenges_table):
    """Opens README.md, creates and fills table with challenges."""
    with open('README.md', 'w') as work_file:
        # Deleting all previous records
        work_file.seek(0)
        work_file.truncate()

        readme_header = (
        "# Reddit Daily Programmer\n",
        "Repository for [r/DailyProgrammer](https://www.reddit.com/r/dailyprogrammer) challenges.\n"
        )

        table_header = (
        "\nNumber| Easy | Intermediate | Hard\n",
        "--- | --- | --- | ---\n"
        )

        work_file.writelines(readme_header)
        work_file.writelines(table_header)

        for number in sorted(challenges_table, reverse = True):
            table_row = "%s | %s | %s | %s\n" % (number,
                                            challenges_table[number][0],
                                            challenges_table[number][1],
                                            challenges_table[number][2])
            work_file.write(table_row)

# Create directory tree for the easy / intermediate / hard directories
# Store directory tree
# Retrieve and store (or pass) information about the files (challenge
# number, description, status (done / unfinished)
# Initiate a table in README.md
# Pass files into respective table cells, create url links
# Add how many unfinished challenges there is
# All can be remade to factor in files in arbitrary folders inside
# rDP repository

if __name__ == '__main__':
    a = collect_files()
    b = create_table(a)
    c = fill_table(b)
    create_readme(c)
