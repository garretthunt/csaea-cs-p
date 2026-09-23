import math
f = False
t = True
nums = [34, 52, 3, 64, 32]

print(7 // 2, 7 % 2, -7 // 2)
#predict - 3, 1, -4
#result - 3, 1, -4

print(int(-5.9),math.floor(-5.9))
#predict - -5, -6
#result - -5, -6

print("5" * 3, "5" + "5")
#predict - 125, 10
#result - 555, 55
#reasoning - 5 in quotes in not an interger, so "5" is being multiplied/added as a word

print(2 ** 4, math.pow(2, 4))
#predict - 16, 16
#result - 16, 16.0
#reasoning - math.pow will always return as a float

print(True + True + True)
#predict - ttt
#result - 3
#reasoning - boolean treats True as integer 1

print(0.1 + 0.2 == 0.3)
#predict - True
#result - False
#reasoning - python does not have an exacty binary representation for 0.1, 0.2, 0.3, so their binary roundings accumulate and cause the expression to not be exactly equal to that of 0.3.)

print("Zebra" < "apple")
#predict - True
#result - True
#reasoning - the ASCII composition of the first letter in "apple" is greater than that of "Zebra"

print(not False or True and False)
#predict - True
#result - True

print(nums[-len(nums)])
#predict - 0
#result - 34
#reasoning - -len counts the index of (nums) backwards, landing on 34)

for i in range(10, 0, -3):
    print(i)
#predict - 10, 7, 4, 1
#result - 10, 7, 4, 1

x=5
while x < 10:
    x += 2
    print(x)
#predict - 11
#result - 11