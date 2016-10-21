def largest_digit(number, max_digits=4):
    num_of_digits = len(str(number))
    if num_of_digits > max_digits:
        print("Input number must have %d or less digits." % (max_digits))
        return None

    digits = list(map(int, str(number)))
    while num_of_digits < max_digits:
        digits.insert(0, 0)
        num_of_digits = len(digits)
    return max(digits)

def num_of_digits_max(input_number, max_digits=4):
    """Takes a number and returns a string with number of digits equal
    to max_digits argument. Adds zeroes in front of the number of
    number of digits less than max_digits.

    Args:
        input_number (int): takes any positive integer number.
        max_digits (int): keyword argument that determines how many
            digits returned string will have. Defaults to 4.

    Returns:
        adjusted_number (str): a string that represents a number
            with number of digits equal to max_digits. Empty positions
            filled with zeroes.

    Raises:
        ValueError: If input_number has number of digits bigger than
            max_digits.
    """
    adjusted_number = str(input_number)
    num_of_digits = len(adjusted_number)

    if num_of_digits > max_digits:
        raise ValueError("Input number must have %d or less digits."
                         % (max_digits))

    while num_of_digits < max_digits:
        adjusted_number = '0' + adjusted_number
        num_of_digits += 1

    return adjusted_number


def ordered_digits(input_number, max_digits=4, descending=False):
    """Returns an integer with  its' digits ordered. 
    
    Args:
        input_number (int): input number
        max_digits (int): input_number will be processed as a number
            with max_digits number of digits. Defaults to 4.
        descending (bool): if True returned integer will have its' digits
            in descending order, if False - in ascending. Defaults to False. 
    Returns:
        number (int): an integer with ordered digits 
    """
    adjusted_number = num_of_digits_max(input_number, max_digits=max_digits)

    digits = sorted(adjusted_number, reverse=descending)
    number = int(''.join(digits))
    return number

def desc_digits(input_number, max_digits=4):
    """Returns an integer with  its' digits in a descending order. 
    
    Args:
        input_number (int): input number
        max_digits (int): input_number will be processed as a number
            with max_digits number of digits. Defaults to 4. 
    Returns:
        number (int): an integer with ordered digits 
    """
    return ordered_digits(input_number, descending=True,
                          max_digits=max_digits)

def asc_digits(input_number, max_digits=4):
    """Returns an integer with  its' digits in a descending order. 
    
    Args:
        input_number (int): input number
        max_digits (int): input_number will be processed as a number
            with max_digits number of digits. Defaults to 4. 
    Returns:
        number (int): an integer with ordered digits 
    """
    return ordered_digits(input_number, descending=False,
                          max_digits=max_digits)

def diff_digits(input_number, max_digits=4):
    """Checks whether input_number has two or more different digits.
    
    Args:
        input_number (int): input number
        max_digits (int): input_number will be processed as a number
            with max_digits number of digits. Defaults to 4.
    Returns:
        bool: False if all digits are the same, True of digits are different. 
    """
    input_number = num_of_digits_max(input_number, max_digits=max_digits)

    num_of_diff_digits = len(set(list(str(input_number))))
    if num_of_diff_digits < 2:
        return False
    else:
        return True

def kaprekar(input_number, iterations=0, prev_number=None, max_digits=4):
    """Finds a Kaprekars fixed point in a number with max_digits or less.

    Args:
        input_number (int): input number  
        iterations (int): number of previous iteration of the Kaprekars cycle.
            Service argument. Defaults to 0.
        prev_number (int): previous number in the Kaprekars cycle. Service argument.
            Defaults to None.
        max_digits (int): input_number will be processed as a number
            with max_digits number of digits. Defaults to 4.
    Returns:
        tuple (imput_number (int), iterations (int)):  
    """
    # infinite loop on cycles 
    if input_number == prev_number:
        return (input_number, iterations)

    if not diff_digits(input_number, max_digits=max_digits):
        return (input_number, iterations)
    else:
        subt_result = (desc_digits(input_number, max_digits=max_digits) -
                      asc_digits(input_number, max_digits=max_digits))
        return kaprekar(subt_result,
                        iterations=iterations + 1,
                        prev_number=input_number,
                        max_digits=max_digits)
# nothing here has been tested


if __name__ == "__main__":
    import unittest

    class TestFunctions(unittest.TestCase):

        def test_num_of_digits_max(self):
            self.assertEqual(num_of_digits_max(1234), '1234')
            self.assertEqual(num_of_digits_max(123), '0123')
            self.assertEqual(num_of_digits_max(0), '0000')
            self.assertEqual(num_of_digits_max(1, max_digits=6), '000001')
            # input number have number of digits bigger than max_digits
            with self.assertRaises(ValueError):
                num_of_digits_max(12345, max_digits=4)
                
        def test_desc_digits(self):
            self.assertEqual(desc_digits(1234), 4321)
            self.assertEqual(desc_digits(4040), 4400)
            self.assertEqual(desc_digits(79, max_digits=6), 970000)
            # input number have number of digits bigger than max_digits
            with self.assertRaises(ValueError):
                desc_digits(12345, max_digits=4)
                
        def test_asc_digits(self):
            self.assertEqual(asc_digits(4321), 1234)
            self.assertEqual(asc_digits(4040), 44)
            self.assertEqual(asc_digits(97, max_digits=6), 79)
            # input number have number of digits bigger than max_digits
            with self.assertRaises(ValueError):
                asc_digits(12345, max_digits=4)

        def test_diff_digits(self):
            self.assertTrue(diff_digits(1234))
            self.assertTrue(diff_digits(6, max_digits=3)) # processed as 006
            self.assertFalse(diff_digits(1111))
            self.assertFalse(diff_digits(0, max_digits=3)) # processed as 000
            
        def test_kaprekar(self):
            self.assertEqual(kaprekar(6589)[1], 2) 
        
    unittest.main()