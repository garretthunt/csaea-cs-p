# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp


def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi() # calling the fuction 
say_bye()
say_hi()
say_hi()
say_bye()

# Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a function's PARAMETER

def express_this(e): # e is called a PARAMETER, which is a placeholder for an ARGUMENT 
    return e

expression = express_this(3 + 2)# the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER

print(expression)

def greeter(name):
    return f"Hi {name}"

first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")

print(first, second, third)

def remainder(a, b):
    return a % b

result = remainder(10, 9)
print(result)

def is_far(distance):

    if distance >= 100:
        return "That's far."
    if distance < 100 and distance > 20:
        return "That's not too far."
    if distance < 20 and distance > 0:
        return "That's close by."
    if distance == 0:
        return "That's right here."
    if distance < 0:
        return "???"

distance_one = is_far(100)
distance_two = is_far(50)
distance_three = is_far(1)
distance_four = is_far(0)
distance_five = is_far(-10)
print(distance_one)
print(distance_two)
print(distance_three)
print(distance_four)
print(distance_five)

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number
# Write a function named doubler() that has TWO parameters: 
# First parameter:  the number i want doubled
# Second paramater: how many times the loop should run 

list = []
# num = int(input("Enter number: "))
# times = int(input("Enter times doubled: "))
def inputs(num, times):
    return num * 2 ** times

result = inputs(__, __)
list.append(result)
print(list)
