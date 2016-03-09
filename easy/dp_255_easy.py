"""
[2016-02-22] Challenge #255 [Easy] Playing with light switches
https://tinyurl.com/dp-255-easy
"""
# Status: DONE
# no bonus
# I should try to use a more efficient way of doing things
# Possible solutions: 
#   - sets
#   - intervals
# What is the best way to solve this problem if we have a list
# of flips beforehand? What if flip intervals are randomly generated?
# How different those solutions will be?
  
from random import randint

def create_switches(num_of_switches):
    """Creates a row of switches."""
    switches = [0] * num_of_switches
    return switches
    
def flip_switches(switches, start, stop):
    if stop < start:
        start, stop = stop, start
    for i in range(start, stop):
        #switches[i] = flip(switches[i])
        if switches[i] == 0:
            switches[i] = 1
        else:
            switches[i] = 0
    
    return switches
    
        
def sum_switches(switches):
    return sum(switches)
    
if __name__ == '__main__':
    num_of_switches = 500000
    num_of_flips = 20000
    
    switches = create_switches(num_of_switches)
    
    for i in range(num_of_flips):
        start = randint(0, num_of_switches)
        stop = randint(0, num_of_switches)
        flip_switches(switches, start, stop)
        
    print(sum_switches(switches))
