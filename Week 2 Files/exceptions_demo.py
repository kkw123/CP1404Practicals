"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user has entered an input that is unable to be process by the formula 
2. When will a ZeroDivisionError occur?
When the program has to divide an interger by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
I could loop the code back if the user enters a 0 as an input.
"""

while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        break;
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")
