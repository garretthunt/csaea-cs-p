import math 

whole = input("Number: ")
num = 0.5 * (guess + whole/guess)
sqrt = math.sqrt(num)

while sqrt != num:
    num = 0.5 * (guess + whole/guess)
    