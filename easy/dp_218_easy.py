"""
[2015-06-08] Challenge #218 [Easy] Making numbers palindromic
https://tinyurl.com/dp-218-easy
"""
    
def calculate_palindrome(number, STEPS = 10000):
    """Calculates palindromic number. Returns (palindrome, counter).
    Returns None if no palindrome exists for this number."""
    counter = 0 
    
    while counter < STEPS:
        if number == number[::-1]:
            return (number, counter) 
    
        counter += 1
        number = str(int(number) + int(number[::-1]))
        
    else: 
        return None 

input_number = input("Enter a number please.\n>")
palindrome = calculate_palindrome(input_number)

if palindrome:
    print("%s gets palindromic after %s steps: %s" % (input_number, 
          palindrome[1], palindrome[0]))
else:
    print("%s not a palindromic number" % input_number)
