"""
[2015-11-02] Challenge #239 [Easy] A Game of Threes
https://tinyurl.com/dp-239-easy
"""
# Status: Done

def input_number():
    number = int(input('> '))
    return number

def modulus(number):
    if number == 1 or number == 0:
        print(number)
        return

    number_initial = number
    mod = number % 3

    if mod == 0:
        operator = '0'
    elif mod == 1:
        operator = '-1'
        number = number - 1
    elif mod == 2:
        operator = '+1'
        number = number + 1

    print(number_initial, operator)
    number = int(number / 3)

    modulus(number)

if __name__ == '__main__':
    modulus(input_number())

        