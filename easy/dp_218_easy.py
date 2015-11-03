"""
[2015-06-08] Challenge #218 [Easy] Making numbers palindromic
https://tinyurl.com/dp-218-easy
"""
    
def calculate_palindrome(number, STEPS = 10000):
    """Calculates palindromic number. Returns (palindrome, counter).
    Returns None if no palindrome exists for this number."""
    
    for i in range(STEPS):
        if number == number[::-1]:
            return (number, i) 
        number = str(int(number) + int(number[::-1]))
    else: 
        return None 


palindromes = dict()
lychrel_numbers = list()

for number in range(1, 1001):
    try:
        palindrome = calculate_palindrome(str(number))[0]
        print(number, palindrome) # print test
    except TypeError: 
        lychrel_numbers.append(number)
        continue  
    
    if palindrome not in palindromes.keys():
        palindromes[palindrome] = [] 
    
    palindromes[palindrome].append(number)
   
print(lychrel_numbers)
    