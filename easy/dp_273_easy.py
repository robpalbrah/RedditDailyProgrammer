"""
[2016-06-27] Challenge #273 [Easy] Getting a degree
https://tinyurl.com/dp-273-easy
"""
# Status: Done

import math

def radian_to_degree(num, precision=2):
    """Convert radiant to degrees with given precision."""
    return round(num * 180 / math.pi, precision)

def degree_to_radian(num, precision=2):
    """Convert degrees to radiant with given precision."""
    return round(num * math.pi / 180, precision)

def below_absolute_zero(num, scale):
    """Check whether given num temperature in unit scale below absolute zero.

    Args:
        num (float): temperature value.
        scale (string): one character string indicating measurement scale
            of num.

    Returns:
        bool: True is num below absolute zero, False otherwise.
    """
    absolute_zero = {'C': -273.15,      # degrees Celsius
                     'K': 0,            # degrees Kelvin
                     'F': -459.67}      # degrees Fahrenheit

    if num < absolute_zero[scale.upper()]:
        print("Value given for conversion is below absolute zero.")
        return True
    else:
        return False

def celsius_to_fahrenheit(num, precision=2):
    """Convert degrees Celsius to degrees Fahrenheit with given precision."""
    if not below_absolute_zero(num, 'c'):
        return round(num * 9/5 + 32, precision)

def celsius_to_kelvin(num, precision=2):
    """Convert degrees Celsius to degrees Kelvin with given precision."""
    if not below_absolute_zero(num, 'c'):
        return round(num + 273.15, precision)

def fahrenheit_to_celsius(num, precision=2):
    """Convert degrees Fahrenheit to degrees Celsius with given precision."""
    if not below_absolute_zero(num, 'f'):
        return round((num - 32) * 5/9, precision)

def fahrenheit_to_kelvin(num, precision=2):
    """Convert degrees Fahrenheit to degrees Kelvin with given precision."""
    if not below_absolute_zero(num, 'f'):
        return round((num + 459.67) * 5/9, precision)
# TODO two functions
def kelvin_to_celsius(num, precision=2):
    """Convert degrees Kelvin to degrees Celsius with given precision."""
    if not below_absolute_zero(num, 'k'):
        return round(num - 273.15, precision)

def kelvin_to_fahrenheit(num, precision=2):
    """Convert degrees Kelvin to degrees Celsius with given precision."""
    if not below_absolute_zero(num, 'k'):
        return round(num * 9/5 - 459.67, precision)

conversion_commands = {'rd': radian_to_degree,
                       'dr': degree_to_radian,
                       'cf': celsius_to_fahrenheit,
                       'ck': celsius_to_kelvin,
                       'fc': fahrenheit_to_celsius,
                       'fk': fahrenheit_to_kelvin,
                       'kc': kelvin_to_celsius,
                       'kf': kelvin_to_fahrenheit}

def process_conversion(command):
    """Perform unit conversion.

    Args:
        command (string): number fallowed, without spaces, by two letters.
            First letter indicates current unit of measurement, second -
            unit that number will be converted into.

            For temperature conversions given number should be above
            absolute zero.

    Returns:
        float: converted value.
    """
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
    angles = ['3.1416rd', '90dr']
    temperatures = ['150ck', '-27.7cf',                 # Celsius
                    '23.11kc', '333.92kf',              # Kalvin
                    '222.81fc', '-11.3fk']              # Fahrenheit
    below_zero = ['-351.1ck', '-0.001kf', '-993fc']

    print("\nangles:")
    for item in angles:
        print(item, ':', process_conversion(item))

    print("\ntemperatures:")
    for item in temperatures:
        print(item, ':', process_conversion(item))

    print("\nbelow zero:")
    for item in below_zero:
        print(item, ':', process_conversion(item))


