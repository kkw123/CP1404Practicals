"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""

import doctest
from Week10Files.car10 import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return [s for n in range(n)]


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert ' '.join(repeat_string("Python", 1)) == "Python"
    # the test below should fail
    assert ' '.join(repeat_string("hi", 2)) == "hi hi"
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, 'Fuel is supposed to be at 10'

    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)


run_tests()

# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# (don't change the tests, change the function!)

# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass

def make_sentence(phrase):
    """
    Change the phrase into a sentence
    >>> make_sentence("Hello")
    'Hello.'
    >>> make_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> make_sentence('noo')
    'Noo.'
    """
    sentence = list(phrase)
    if not sentence[0].isupper():
        sentence[0] = sentence[0].upper()
    if sentence[-1] != '.':
        sentence.append('.')
    return ''.join(sentence)
