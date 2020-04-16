"""
CP1404/CP5632 Practical

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""


def main():
    user_input = input('Enter a string: ').strip()
    word_to_counts = check_string(user_input)
    longest_word_length = max([len(word) for word in word_to_counts.keys()])
    for word, count in word_to_counts.items():
        print('{:{}} = {}'.format(word, longest_word_length , count))


def check_string(string1):
    words = string1.split(' ')
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


main()
