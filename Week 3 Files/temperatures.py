"""
CP1404 Practicals

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

def main():
    temp_celsius = float(input('Enter temperature in celsius: '))
    temp_fahrenheit = float(input('Enter temperature in fahrenheit: '))
    celsius_to_fahrenheit(temp_celsius)
    fahrenheit_to_celsius(temp_fahrenheit)


def celsius_to_fahrenheit(temp):
    fahrenheit = (temp*1.8) + 32
    print('{:.2f}'u'\u2103'' is {:.2f}'u'\u2109'.format(temp,fahrenheit))

def fahrenheit_to_celsius(temp):
    celsius = (5*(temp-32))/9
    print('{:.2f}'u'\u2109'' is {:.2f}'u'\u2103'.format(temp, celsius))


main()