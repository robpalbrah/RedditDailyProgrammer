# [2015-08-24] Challenge #229 [Easy] The Dottie Number
# https://www.reddit.com/r/dailyprogrammer/comments/3i99w8/20150824_challenge_229_easy_the_dottie_number/

import math 

def foxed_cox(number):
    """Finds a fixed point of cosine"""
    cos_number = math.cos(number)
    print(cos_number)
    
    difference = math.fabs((number - cos_number) / number)    
    if difference < 1e-6:
        print('DIFFERENCE: %s' % difference)
        return cos_number
    else:
        fixed_cos(cos_number)


input_number = float(input('>'))        
fixed_cos(input_number)        