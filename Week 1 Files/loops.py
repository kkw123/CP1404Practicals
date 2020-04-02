def one_to_twenty_oddNumbers():  # Prints odd numbers from 1 to 20
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()


def zero_to_hundred_inTens():      #Prints in tens from 0 to hundred
    for i in range(0, 101, 10):
        print(i, end=' ')
    print()


def twenty_to_one_numberDown():     #Prints all numbers from 20 to 1
    for i in range(20, 0, -1):
        print(i, end=' ')
    print()


def print_custom_stars():
    stars = int(input('Number of stars: '))     #Prints the number of stars requested from user
    for i in range(1, stars + 1, 1):
        print('*', end='')


print_custom_stars()
