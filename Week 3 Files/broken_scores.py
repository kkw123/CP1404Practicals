"""
CP1404 Practicals

Name: Kum King Wye
Github link: https://github.com/kkw123/CP1404Practicals

"""

def main():
    score = int(input("Enter your score: "))
    result = checkScore(score)
    print(result)


def checkScore(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score > 80:
        return "A+"
    elif score > 74:
        return "A"
    elif score > 64:
        return "B"
    elif score > 49:
        return "C"
    else:
        return "Fail"


main()