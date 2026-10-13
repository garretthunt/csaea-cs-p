import random

# USER INPUT IN PYTHON
#print("<PROMPT>")

# name = input("Enter your name: ")
# print(f"Hello {name}")

# print(type(name))

# age = input("Enter your age: ")
# print(f"Your age is {age}")

# print(type(age))

# age_converted = int(age)
# print(type(age_converted))

# height = float(input("Enter your height: "))
# print(f"You are {height} meters tall")
# print(height + 1)


# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

color = input("Enter your favorite color: ")
print(f"Your favorite color is {color}")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
result = number_one + number_two
print(f"Your result is {result}")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.

diameter = int(input("Enter your diameter: "))
radius = diameter/2
pi = 3.14
circle_area = pi * radius ** 2
print(f"Your circle's area is {circle_area}")

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

sides_die = int(input("Enter your desired number of sides on your die: "))
number = random.randint(1,sides_die)
print(f"Your rolled number is {number}")