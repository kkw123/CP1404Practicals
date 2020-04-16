"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


def main():
    user_input = input('Enter a string: ').strip()
    counts_per_word = check_string(user_input)
    for word, count in counts_per_word.items():
        print('{:{}} = {}'.format(word, 10, count))


def check_string(string1):
    words = string1.split(' ')
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


def check_longest_word(dict1):
    longest_word = str()
    for word in dict1:
        if len(word) > longest_word:
            longest_word = word
    return longest_word


main()
