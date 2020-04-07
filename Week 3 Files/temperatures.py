"""
CP1404 Practicals

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

def main():
    original_celsius = float(input('Enter temperature in celsius: '))
    original_fahrenheit = float(input('Enter temperature in fahrenheit: '))
    converted_to_fahrenheit = celsius_to_fahrenheit(original_celsius)
    converted_to_celsius = fahrenheit_to_celsius(original_fahrenheit)
    print('{:.2f} degrees celsius is {:.2f} degrees fahrenheit'.format(original_celsius , converted_to_fahrenheit))
    print('{:.2f} degrees fahrenheit is {:.2f} degrees celsius'.format(original_fahrenheit , converted_to_celsius))


def celsius_to_fahrenheit(temp):
    fahrenheit = (temp*1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(temp):
    celsius = (5*(temp-32))/9
    return celsius


main()