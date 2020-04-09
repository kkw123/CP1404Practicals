"""
CP1404 Practicals

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""
import random
FIRST_NUMBER = 1
LAST_NUMBER = 45
NUMBER_PER_DRAW = 6


def main():
    amt_of_draws = int(input('How many quick picks? '))
    for draws in range(amt_of_draws):
        make_draw()


def make_draw():
    drawn_numbers = []
    current_number = int()
    while len(drawn_numbers) != NUMBER_PER_DRAW:
        current_number = random.randint(FIRST_NUMBER-1,LAST_NUMBER)
        if current_number not in drawn_numbers:
            drawn_numbers.append(current_number)
    display_numbers = ' '.join([str(num) for num in drawn_numbers])
    print(display_numbers)


main()
