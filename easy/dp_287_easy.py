"""
[2016-10-10] Challenge #287 [Easy] Kaprekar's Routine
https://tinyurl.com/dp-287-easy
"""
# Status: Done

# Additional challenge: create a table similar to the table
# in Wiki https://en.wikipedia.org/wiki/6174_(number)
# Digits of the given number | Cycles | Cycles length | Number of cycles 

def num_of_digits_max(input_number, max_digits=4):
    """Returns a string with number of digits equal to max_digits
    argument. Inserts zeroes at the front of the string if number
    of digits less than max_digits.

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
    adjusted_number = num_of_digits_max(input_number, max_digits)

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
    return ordered_digits(input_number, max_digits, descending=True)

def asc_digits(input_number, max_digits=4):
    """Returns an integer with  its' digits in a descending order.

    Args:
        input_number (int): input number
        max_digits (int): input_number will be processed as a number
            with max_digits number of digits. Defaults to 4.
    Returns:
        number (int): an integer with ordered digits
    """
    return ordered_digits(input_number, max_digits, descending=False)


def kaprekar(input_number, iterations=0, max_digits=4, results_list=None):
    """Finds a Kaprekars fixed point in a number with max_digits or less.

    Args:
        input_number (int): input number
        iterations (int): number of previous iteration of the Kaprekars cycle.
            Service argument. Defaults to 0.
        max_digits (int): input_number will be processed as a number
            with max_digits number of digits. Defaults to 4.
        results_list (list): list of all previous results of kaprekar function.
            Used to detect cycles.
    Returns:
        tuple (fixed_point (int), iterations (int)): two-tuple returned if
            there is a fixed point of Kaprekars function.
        tuple (cycle_start (int), iterations (int), cycle_list (list):
            three-tuple returned if there is a cycle
    """
    if results_list is None:
        results_list = []
    subt_result = (desc_digits(input_number, max_digits) -
                      asc_digits(input_number, max_digits))
    if subt_result == input_number:
        return (subt_result, iterations)
    elif subt_result in results_list:
        cycle_list = results_list[results_list.index(subt_result):]
        return (subt_result, iterations, cycle_list)
    else:
        results_list.append(subt_result)
        return kaprekar(subt_result, iterations+1, max_digits, results_list)


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

        def test_kaprekar(self):
            self.assertEqual(kaprekar(6589), (6174,2))
            self.assertEqual(kaprekar(5455), (6174,5))
            self.assertEqual(kaprekar(6174), (6174,0))

    unittest.main()