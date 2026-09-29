import math

#1. Tip Calculator
bill = 50
tip = bill * 2 / 10
print(tip)

#2. Temperature Converter
fahrenheit = 212
halfway = fahrenheit - 32
celcius = halfway * 5 / 9
print(celcius)

#3. Report Card
score = 84
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score < 60:
    print("F")

#4. Rollar Coaster Gate
height = 48
age = 8
has_adult = True

if height >= 48 and age > 10 or height >= 48 and age < 10 and has_adult == True:
    print("You may ride!")

#5. Name Tag Generator
first = "Ada"
last = "Lovelace"
school = "CSAEA"

print(f"Hello, my name is {first} {last} from {school}")

for i in range(10, -1, -1):
    if i > 0:
        print(i)
    if i == 0:
        print ("Liftoff!")

#6. Garden Fence

area = 49
side = math.sqrt(area)
perimiter = side * 4

print(f"{perimiter} ft")

#7. Parking Meter

minutes_parked = 50
block_length = 15
cost_per_block = 1

initial = minutes_parked // block_length 
remainder = minutes_parked % block_length 
if remainder > 0: 
    blocks = initial + 1 
elif remainder == 0: 
    blocks = initial
money = blocks * cost_per_block 

print(f"You owe ${money}")

#8. Leap Year Checker

year = 1900

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#9. Speed Trap

speed_limit = 55
speed = 71

if speed % speed_limit > 0 and speed % speed_limit < 11:
    print("Warning!")
elif speed % speed_limit > 10 and speed % speed_limit < 21:
    print("Fine: $100")
else:
    print("Fine: $200")

#10. Times Table Helper

number = 7

for i in range(1,11):
    print(f"{number * i}")

#11. Login Screen

password = "csaea2026"
attempt = "CSAEA2026"

if password == attempt:
    print("Access granted")
else:
    print("Access denied")

#12. Even/Odd Parking

plate = 4827

if plate % 2 == 0:
    print("Park on the east side")
else:
    print("Park on the west side")
