"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        input1 = int(input('Please a number: '))
        break;
    except ValueError:  
        print("Please enter a valid integer.")
result = input1
print("Valid result is:", result)
