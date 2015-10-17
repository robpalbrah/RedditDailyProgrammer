# [2015-08-17] Challenge #228 [Easy] Letters in Alphabetical Order
# https://www.reddit.com/r/dailyprogrammer/comments/3h9pde/20150817_challenge_228_easy_letters_in/

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
  