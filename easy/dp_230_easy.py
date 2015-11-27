"""
[2015-08-31] Challenge #230 [Easy] JSON treasure hunt
https://tinyurl.com/dp-230-easy
"""

import json

a = "{ 'cats' : ['neat', 'lovely'], 'dogs' : [7, 'fine too']}"
class Cat(json.JSONDecoder): 
    pass
b = Cat()