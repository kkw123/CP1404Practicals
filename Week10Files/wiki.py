"""
CP1404/CP5632 Practical
Wiki
Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals
"""
import wikipedia


def main():
    user_input = input('Write page title or search -> ')
    while user_input != '':
        try:
            page = wikipedia.page(user_input)
        except wikipedia.exceptions.DisambiguationError as e:
            for index in range(4):  # list 4 options
                print(e.options[index])
        else:
            print(page.title)
            print(page.summary)
            print(page.url)
        user_input = input('Write page title or search -> ')
    print('End')



main()
