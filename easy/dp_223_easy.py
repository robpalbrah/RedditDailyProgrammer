# [2015-07-13] Challenge #223 [Easy] Garland words
# https://www.reddit.com/r/dailyprogrammer/comments/3d4fwj/20150713_challenge_223_easy_garland_words/

# Add optional challenges. 
def garland(word):
    """
    Takes a word and determines it's garland number. 
    Returns (word, g_number). 
    """
    g_number = 0 
    for num in range(1, len(word)):
        if word[:num] == word[-num:]:
            g_number = num 
            
    return(g_number)
   
def optional_one(word):
    """Optional challenge one."""
    g_number = garland(word)
    
    if g_number > 0:
        print(word[:g_number + 1]*2 + word + '...')
    else:
        print("Not a garland word")

 
def optional_two():  
    """Optional challenge two."""
    file = open(r'C:\code\rDP\enable1.txt', 'r')

    g_number = 0  
    for word in file.readlines():
        number = garland(word.rstrip())
        if number > g_number:
            g_number = number
            g_word = word.rstrip() 

    if g_number > 0:
        print("garland('%s') -> %d\n" % (g_word, g_number))    
    else: 
        print('No garland words in given set')
       
optional_one('onion')    