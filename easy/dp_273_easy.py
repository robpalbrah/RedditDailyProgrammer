"""
[2016-06-27] Challenge #273 [Easy] Getting a degree
https://tinyurl.com/dp-273-easy
"""
import math

conversion_commands = {'rd': radian_to_degree,
                       'dr': degree_to_radian,
                       'cf': celsius_to_fahrenheit,
                       'ck': celsius_to_kelvin,
                       'fc': fahrenheit_to_celsius,
                       'fk': fahrenheit_to_kelvin,
                       'kc': kelvin_to_celsius,
                       'kf': kelvin_to_fahrenheit}

def radian_to_degree(num):
    """Convert radiant to degrees with two digit precision."""
    return round(num * 180 / math.pi, 2)

def degree_to_radian(num):
    """Convert degrees to radiant with two digit precision."""
    return round(num * math.pi / 180, 2)

def below_absolute_zero(num, scale):
    absolute_zero = {'C': -273.15,  # degrees Celsius
                     'K': 0,        # degrees Kelvin
                     'F': -459.67   # degrees Fahrenheit

    if num < absolute_zero[scale.upper()]:
        print("Value given for conversion is below absolute zero.")
        return True
    else:
        return False

def celsius_to_fahrenheit(num):
    """Convert degrees Celsius to degrees Fahrenheit
    with two digit precision."""
    if not below_absolute_zero(num, 'c'):
        return round(num * 9/5 + 32, 2)

def celsius_to_kelvin(num):
    """Convert degrees Celsius to degrees Kelvin with two
    digit precision."""
    if not below_absolute_zero(num, 'c'):
        return round(num + 273.15, 2)

def fahrenheit_to_celsius(num):
    """Convert degrees Fahrenheit to degrees Celsius with two
    digit precision."""
    if not below_absolute_zero(num, 'f'):
        return round((num - 32) * 5/9, 2)

def fahrenheit_to_kelvin(num):
        """Convert degrees Fahrenheit to degrees Kelvin with two
    digit precision."""
    if not below_absolute_zero(num, 'f'):
        return round((num + 459.67) * 5/9, 2)
# TODO two functions        
def kelvin_to_celsius(num):
    pass 

def kelvin_to_fahrenheit(num):
    pass
    
def process_conversion(command):
    # TODO docstring
    try:
        num, convert = float(command[0:-2]), command[-2:]
    except ValueError:
        print('Value Error. Invalid input.')
    else:
        if convert in conversion_commands:
            return conversion_commands[convert](num)
        else:
            print("No candidate for conversion")

if __name__ == '__main__':
    process_conversion('aaaa')


