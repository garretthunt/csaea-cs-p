#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 7 + 24
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 10 / 3
print("Float division:", float_divide)

integer_divide = 7 // 2
print("integer_divide:", integer_divide)

mod = 7 % 2
print("Modulus:", mod)

exponent = 7 ** 2
print("Exponent:", exponent)

#PEMDAS (parentheses, exponents, multiplication/division, addition/subtraction)

result1 = (2 + 3) * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result 3:", result3)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.  

width = 8
base = 5
area = width * base
print("Area:", area)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. (Use 3.14 for π.)  

radius = 7
pi = 3.14
area = pi * radius ** 2
print("Area:", area)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.  

book_cost = 12.99
book_count = 3
notebook_cost = 3.50
notebook_count = 4
total = book_cost * book_count + notebook_cost * notebook_count
print(f"Book: ${book_cost} \nNotebook: ${notebook_cost} \nTotal: ${total}")

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd. 

num = 57
if num % 2 == 0:
    print("Num: Even")
else:
    print("Num: Odd")
