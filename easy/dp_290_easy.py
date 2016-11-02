"""
[2016-10-31] Challenge #290 [Easy] Kaprekar Numbers
https://tinyurl.com/dp-290-easy
"""

# works only for base 10
def is_kaprekar_number(input_number):
    input_squared = str(input_number ** 2)
    num_of_digits = len(input_squared)

    # range function starts with 1 since
    # input_squared is devided into two parts
    for i in range(1, num_of_digits):
        first_part = int(input_squared[:i])
        second_part = int(input_squared[i:])

        if first_part == 0 or second_part == 0:
            continue
        else:
            sum_parts = first_part + second_part
            if sum_parts == input_number:
                return True
    else:
        return False

def range_kaprekar(start, end):
    kaprekar_numbers = []
    for n in range(start, end+1):
        if is_kaprekar_number(n):
            kaprekar_numbers.append(n)
    return kaprekar_numbers

if __name__ == '__main__':
    print(range_kaprekar(101, 9000))