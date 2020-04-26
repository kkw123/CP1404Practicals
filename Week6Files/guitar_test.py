"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

from Week6Files.guitar import Guitar


def main():
    guitars = []
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # test code 1
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # test code 2
    print('My Guitars!')
    while True:
        name = input('Name: ')
        if not name:
            break
        year = int(input('Year: '))
        cost = float(input('Cost: '))
        guitars.append(Guitar(name, year, cost))
    print('...snip...')
    count = 0
    for i, guitar in enumerate(guitars, 1):
        print('Guitar {}: {}'.format(i, guitar))


main()
