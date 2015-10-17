# [2015-07-06] Challenge #222 [Easy] Balancing Words
# https://www.reddit.com/r/dailyprogrammer/comments/3c9a9h/20150706_challenge_222_easy_balancing_words/

def balance(word):
    """
    Determines balance point of a word. Takes str. Returns None. 
    
    Prints words split by their balance point and the weight on either side
    Prints "word DOES NOT BALANCE" if the word have no balance point. 
    """
    word = word.upper()
    letters = [letter for letter in word] 
    letters_ord = [ord(letter) - 64 for letter in letters] # ord('A') - 64 = 1
    
    length = len(letters)
    
    for bal_point in range(1, length - 1):
        # we exclude first and last letters from being a balance points
        
        position_list = [] 
        for index in range(length):
            position = abs(bal_point - index)
            position_list.append(position)
        
        value_list = []
        for index in range(length):
            value = position_list[index] * letters_ord[index]
            value_list.append(value)
        
        weight = sum(value_list[ : bal_point])
        
        if weight == sum(value_list[bal_point + 1 : ]):
            print('%s %s %s - %d' % (word[ : bal_point], word[bal_point],
                                     word[bal_point + 1 : ], weight))
            break
    
    else:
        print("%s DOES NOT BALANCE" % word)

        
challange_list = [
'CONSUBSTANTIATION',
'WRONGHEADED',
'UNINTELLIGIBILITY',
'SUPERGLUE',
'ABA',
'BABE']

for challange in challange_list:
    balance(challange)
    