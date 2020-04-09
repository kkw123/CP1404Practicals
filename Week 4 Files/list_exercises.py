"""
CP1404 Practicals

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""


def main():
    no_of_numbers = 5
    i = 0
    numbers = []
    while i < no_of_numbers:
        user_input = numbers.append(int(input('Number: ')))
        i += 1
    average = sum(numbers) / len(numbers)
    print('The first number is {}'.format(numbers[0]))
    print('The last number is {}'.format(numbers[4]))
    print('The smallest number is {}'.format(min(numbers)))
    print('The largest number is {}'.format(max(numbers)))
    print('The average of the numbers is {}'.format(average))


main()
