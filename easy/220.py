# [2015-06-22] Challenge #220 [Easy] Mangling sentences
# https://tinyurl.com/rDP-220-Easy
import string


def mangle_word(word):
    """Takes a single word and arranges it's letters in alphabetical order.
    Leaves numbers and punctuation in place. Capital letters retain their 
    positions. Returns mangles word."""
    if not len(word):
        return word 
        
    # Searching for capital letters
    capital_letters = [] 
    for (index, letter) in enumerate(word):
        if letter.isupper():
            capital_letters.append(index)
    
    # Searching for punctuation and numbers 
    fixed_points = []
    for (index, letter) in enumerate(word):
        if letter in string.punctuation:
            fixed_points.append(index)
        if letter.isdigit():
            fixed_points.append(index)
    
    word = word.lower()
    sorting_list = [letter for letter in word]

    # Removing punctuation and numbers 
    if fixed_points:
        for point_index in reversed(fixed_points):
            del sorting_list[point_index]
     
    sorting_list.sort()
    sorting_list = [letter for letter in sorting_list]
    
    # Adding back punctuation, numbers and capital letters     
    if fixed_points:
        for point_index in fixed_points: 
            sorting_list.insert(point_index, word[point_index])
            
    if capital_letters:
        for capital_index in capital_letters:
            sorting_list[capital_index] = sorting_list[capital_index].upper()
    
    mangled_word = ''.join(sorting_list)
    
    return mangled_word
  
def mangle_sentence(sentence):
    """Takes a str and puts letters in words in alphabetical
    order. Returns mangled sentence"""
    if ' ' in sentence:
        sentence = sentence.split()
        sentence = [mangle_word(word) for word in sentence]
        mangled_sentence = ' '.join(sentence)
    else: 
        mangled_sentence = mangle_word(sentence)
        
    return mangled_sentence
            

challange_inputs = {
'input1' : "Eye of Newt, and Toe of Frog, Wool of Bat, and Tongue of Dog.",
'input2' : """Adder's fork, and Blind-worm's sting, Lizard's leg, and 
              Howlet's wing.""",
'input3' : """For a charm of powerful trouble, like a hell-broth boil 
              and bubble."""
}
              
if __name__ == '__main__':
    
    for key in challange_inputs:
        print('%s:\n' % key, mangle_sentence(challange_inputs[key]))