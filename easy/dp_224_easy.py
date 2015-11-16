"""
[2015-07-20] Challenge #224 [Easy] Shuffling a List
https://tinyurl.com/dp-224-easy
"""
# Status: Done

import copy
import math 
import random 


input_list = [1, 2, 3, 4]

def faro_shuffle(input_list):
    """
    Splits list into half's and then interweaves them perfectly.   
    """
    half = int(math.ceil(len(input_list) / 2))
    first_half = input_list[0:half]
    second_half = input_list[half:] 
    
    num_of_elem = len(first_half)
    faro_list = []
    
    for n in range(0, num_of_elem):
        try:
            faro_list.append(first_half[n])
            faro_list.append(second_half[n])
        except IndexError: 
            pass
        
    return faro_list
    
def fisher_yates_shuffle(input_list):
    """
    Fisher - Yates algorithm for generating a random permutation. 
    """
    list_length = len(input_list)
    fisher_yates_list = [] 
    work_list = input_list[:]
    
    for n in range(list_length):
        rand = random.randint(0, list_length - 1)
        elem = work_list.pop(rand)
        
        fisher_yates_list.append(elem)
        
        list_length -= 1

    return fisher_yates_list

def permutation_checker(input_list, permut_number = 100000):
    """
    Checks randomness of fisher_yates_shuffle.
    Returns dictionary {"elem1" : [index1, probability, ...], ...}
    """
    index_list = [[index, 0] for index in range(len(input_list))]
    pc_dict = {}
    
    for elem in input_list:
        pc_dict[elem] = copy.deepcopy(index_list)
        
    for n in range(permut_number):
        work_list = fisher_yates_shuffle(input_list)

        for elem in work_list:
            index = work_list.index(elem)
            pc_dict[elem][index][1] += 1
    
    for elem in pc_dict:
        for pair in pc_dict[elem]:
            pair[1] = pair[1] / permut_number
            
    return pc_dict

function_check = permutation_checker(input_list)     
for key in function_check:
    print(key, function_check[key])