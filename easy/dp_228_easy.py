"""
[2015-08-17] Challenge #228 [Easy] Letters in Alphabetical Order
https://tinyurl.com/dp-228-easy
"""
# Status: Done

def alph_order(word):
    """
    Function takes a string and determines wither or not 
    characters in alphabetical or reversed alphabetical order.
    """
        
    if word == ''.join(sorted(word)):
        print('%s IN ORDER' % word)
    elif word == ''.join(sorted(word, reverse = True)):
        print('%s REVERSE ORDER' % word)
    else:
        print('%s NOT IN ORDER' % word)
        
input_list = [
'billowy', 
'biopsy', 
'chinos',
'defaced',
'chintz',
'sponged',
'bijoux',
'abhors',
'fiddle',
'begins',
'chimps',
'wronged']

for word in input_list:
    alph_order(word)
  