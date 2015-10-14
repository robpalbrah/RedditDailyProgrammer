# [2015-06-22] Challenge #220 [Easy] Mangling sentences
# https://tinyurl.com/rDP-220-Easy

def mangle_word(word):
    
    # Searching for capital letters
    capital_letters = [] 
    for (index, letter) in enumerate(word):
        if ord(letter) in range(65, 91):
            # ord('A') = 65, ord('Z') = 90
            capital_letters.append(index)
            print('Capital_index: ', index) #print_test
    
    # Searching for punctuation and numbers 
    punctuation_marks = "\",.;:[]{}()!@#$%^&*\/-+|'?<>`~_="
    fixed_points = []
    for (index, letter) in enumerate(word):
        if letter in punctuation_marks:
            print('Punctuation: ', letter) #print_test
            fixed_points.append(index)
        if letter in [str(number) for number in range(10)]:
            print('Number: ', letter) #print_test
            fixed_points.append(index)
    print('fixed points', fixed_points) #print_test
    
    word = word.lower()
    print('word: ', word) #print_test
    sorting_list = [ord(letter) for letter in word]

    # Removing punctuation and numbers 
    if fixed_points:
        for point_index in reversed(fixed_points):
            print('Deleting: ', chr(sorting_list[point_index])) #print_test
            del sorting_list[point_index]
    print([chr(a) for a in sorting_list]) #print_test
     
    sorting_list.sort()
    sorting_list = [chr(letter) for letter in sorting_list]
    
    # Adding back punctuation and numbers    
    if fixed_points:
        for point_index in fixed_points: 
            sorting_list.insert(point_index, word[point_index])
            
    if capital_letters:
        for capital_index in capital_letters:
            sorting_list[capital_index] = sorting_list[capital_index].upper()
    
    mangled_word = ''.join(sorting_list)
    
    return mangled_word
  
print(mangle_word("#deSanta'S123!"))  
            
