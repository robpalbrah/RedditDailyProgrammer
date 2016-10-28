"""
[2016-10-03] Challenge #286 [Easy] Reverse Factorial
https://tinyurl.com/dp-286-easy
"""
# Status: Done

def reverse_factorial(input_number):
    """Takes non-negative integer and returns its reverse factorial.
    Args:
        number(int): input number
    Returns:
        'i!' (str): reverse factorial if in exists, else returns 'NONE'.
            Special case for input_number = 1: returns '0!, 1!'
    """
    if input_number <= 0:
        return 'NONE'
    elif input_number == 1:
        return '0!, 1!'

    number = float(input_number)
    i = 2 # starts from 2 because '1' was handled above
    while number.is_integer():
        number = number / i
        if number == 1:
            return ('%d!' % i)
        else:
            i += 1
    else:
        return 'NONE'

if __name__ == '__main__':
    import unittest

    class TestFunctions(unittest.TestCase):
        def test_reverse_factorial(self):
            self.assertEqual(reverse_factorial(0), 'NONE')
            self.assertEqual(reverse_factorial(1), '0!, 1!')
            self.assertEqual(reverse_factorial(2), '2!')

            self.assertEqual(reverse_factorial(120), '5!')
            self.assertEqual(reverse_factorial(150), 'NONE')
            self.assertEqual(reverse_factorial(3628800), '10!')
            self.assertEqual(reverse_factorial(479001600), '12!')
            self.assertEqual(reverse_factorial(6), '3!')
            self.assertEqual(reverse_factorial(18), 'NONE')

    unittest.main()
