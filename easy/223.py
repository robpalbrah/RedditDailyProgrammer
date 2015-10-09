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
        if word[: num] == word[len(word) - num : ]:
            g_number = num 
            
    return(word, g_number)
    
print(garland('alfalfa'))
            
        
    