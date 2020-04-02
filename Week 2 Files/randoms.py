import random

print(random.randint(5, 20))  
print(random.randrange(3, 10, 2))  
print(random.uniform(2.5, 5.5))

"""
What did you see on line 1?
8
What was the smallest number you could have seen, what was the largest?
5 is the smallest and 20 is the largest

What did you see on line 2?
7
What was the smallest number you could have seen, what was the largest?
3 is the smallest and 9 is the largest
Could line 2 have produced a 4?
Line 2 cannot produce a 4 as 3 cannot add up to 4 using increments of 2

What did you see on line 3?
5.193858683333737
What was the smallest number you could have seen, what was the largest?
Smallest number would be 2.5 and highest would be 5.5

"""

print(random.randint(1,100))
