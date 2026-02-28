#code 1
# area of circle
'''
r = int(input("Enter the radius of the circle:"))
pie = 3.14
area = pie * r * r
print("The area of the circle is:", area)
'''
#code 2
#sum, difference, product and quotient of two numbers
'''
a = int(input("Enter the first number:"))
b = int(input("Enter the second integer:"))
print(f"sum = {a + b}")
print(f"difference = {a - b}")
print(f"product = {a * b}")
if b == 0:
    print("undefined for quotient and remainder")
else:
    print(f"quotient = {a / b}")
    print(f"remainder = {a % b}")
'''
#code 3
#simple calculator program
'''
a = int(input("Enter the first number:"))
b = int(input("Enter the second integer:"))
o = input("Enter the operator (+, -, *, /):")
if o == "+":
    print(f"sum = {a + b}")
elif o == "-":
    print(f"differnce = {a - b}")
elif o == "*":
    print(f"product = {a * b}")
elif o == "/":
    if b == 0:
      print("undefined for division")
    else:
      print(f"division = {a / b}")
else:
    print("INVALID INPUT")
'''
#code 4
#find area and perimeter of a rectangle
'''
l = int(input("Enter the length of the rectangle:"))
b = int(input("Enter the breadth of the rectangle:"))
if l <= 0 or b <= 0:
    print("Invalid input! Length and breadth must be positive.")
else:
    print(f"Area of the rectangle is {l * b}")
    print(f"Perimeter of the rectangle is {2 * (l + b)}")
'''
#code 5
#check if a number is positive, negative or zero
'''
a = int(input("Enter a number:"))
if a > 0:
    print("The given number is Positive")
elif a < 0:
    print("The given number is Negative")
else:
    print("The given number is Zero")
'''
#code 6
# displays whether a < b, a = b, or a > b.
''' 
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a = b")
'''
#code 7
#takes three integers as input and prints their maximum value.
'''
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a >= b and a >= c :
    print(f"The maximum value is {a}")
elif b >= a and b >= c:
    print(f"The maximum value is {b}")
else:    
    print(f"The maximum value is {c}")
'''
#code 8
#takes three-digit integer as input and prints the sum of its digits.
'''
d = int(input("Enter a three-digit integer:"))
if d < 100 or d > 999:
    print("Invalid input! Please enter a three-digit integer.")
else:
    sum_of_digits = (d // 100) + ((d % 100) // 10) + (d % 10)
    print(f"The sum of the digits is {sum_of_digits}")
'''
#code 9
#takes 5 subjects marks as input and prints the total marks and percentage.
'''
s1 = int(input("Enter the marks of the first subject:"))
s2 = int(input("Enter the marks of the second subject:" ))
s3 = int(input("Enter the marks of the third subject:"))
s4 = int(input("Enter the marks of the fourth subject:"))
s5 = int(input("Enter the marks of the fifth subject:"))
total_marks = s1 + s2 + s3 + s4 + s5
percentage = (total_marks / 500) * 100
print(f"Total marks: {total_marks}")
print(f"Percentage: {percentage}%")
'''
#code 10
#takes 3 integers as input and prints the minimum value:
'''
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a <= b and a <= c:
    print(f"The minimum value is {a}")
elif b <= a and b <= c:
    print(f"The minimum value is {b}")
else:
    print(f"The minimum value is {c}")
'''
#code 11
#odd or even
'''
a = int(input("Enter a number:"))
if a % 2 == 0:
    print("The given number is Even")
else:
    print("The given number is Odd")
'''
#code 12
#takes floating point value as input and prints its absolute value
#type casting
'''
a = float(input("Enter a floating point number:"))
print(f"The absolute value is {int(a)}")
'''
#code 13
#takes an integer as input and checks if it is divisible by 17
'''
a = int(input("Enter an integer:"))
if a % 17 == 0:
    print("The given number is divisible by 17")
else:
    print("The number is not divisible by 17")
'''
# code 14
# takes a valid letter grade (S/A/B/C/D/E) as input&prints its respective grade point (10/9/8/7/6/4).
'''
grade = (input("Enter the letter grade (S/A/B/C/D/E):"))
if grade == "S":
    print("The grade point is 10")
elif grade == "A":
    print("The grade point is 9")
elif grade == "B":
    print("The grade point is 8")
elif grade == "C":
    print("The grade point is 7")
elif grade == "D":
    print("The grade point is 6")
elif grade == "E":
    print("The grade point is 4")
else:
    print("Invalid input! Please enter a valid letter grade (S/A/B/C/D/E).")
'''
#code 15
# Write a program to select one option from the list and display output accordingly.
# Example:
# Please enter your choice:
# 1. Check Balance
# 2. View Offers
# 3. Special Recharge
# Enter 0 to exit
# (Display some arbitrary message for each option, e.g., “Your balance is Rs. 500”.)
'''
print("Please enter your choice:")
print("1. Check Balance")
print("2. View Offers")
print("3. Special Recharge")
print("Enter 0 to exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Your balance is Rs. 500")
elif choice == 2:
    print("Today's offer: 1GB free data")
elif choice == 3:
    print("Special recharge activated")
elif choice == 0:
    print("Exiting...")
else:
    print("Invalid choice")
'''
#code 16
#takes input for the coefficients of the quadratic equation
# ax2 + bx + c = 0
# and prints whether the roots are real or complex.
'''
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    print("The roots are real and distinct.")
elif discriminant == 0:
    print("The roots are real and equal.")
else:
    print("The roots are complex.")
'''
#code 17

# Write a program that takes two 5-letter words as input and finds the sum of the distance
# between the respective characters of these words.
# Example:
# Input:
# abcde
# abdfe
# Distance: 0-0-1-2-0
# Output: 3
# Input:
# pqxzy
# qpyax
# Distance: 1-1-1-25-1
# Output: 29

word1 = input("Enter the first 5-letter word: ")
word2 = input("Enter the second 5-letter word: ")

# Initialization
total_distance = 0

if len(word1) == 5 and len(word2) == 5:
   
    for i in range(5):
        distance = abs(ord(word1[i]) - ord(word2[i]))
        total_distance += distance
        print(distance, end=' ')  # Print the distance for each character
    print()  # New line for clarity
    print("Total distance:", total_distance) 

else:
    print("Both words must be exactly 5 letters long.")

#code 18
    # Write a program that takes a 2-letter word as input and prints it in capital letters.
    # Note: Each letter of the input word can be in capital or small letters.
'''
word = input("Enter a 2-letter word: ")
if len(word) != 2 or not word.isalpha():
    print("Invalid input! Please enter a 2-letter word.")
else:
    print(f"The word in capital letters is: {word.upper()}")
'''
#code 19
#takes a 2-letter word as input and prints it in small letters.
#Note: Each letter of the input word can be in capital or small letters.
'''
word = input("Enter a 2-letter word:")
if len(word) != 2 or not word.isalpha():
    print("Invalid input! Enter a two letter word")
else:
    print(f"The word in small letters is {word.lower()}")
'''
#code 20
# Write a program that takes a character as input and prints the alpha-numeric character (0–9,
# A–Z, a–z are alpha-numeric characters) that is closest to this character.
# Note: If the input character is equidistant from two alpha-numeric values, either one can
# be printed.

char = input(text)
if char.isalnum():
    print(f"The closest alpha-numeric character is: {char}")
elif char.isalpha():
    if char.islower():
        print(f"The closest alpha-numeric character is: {char.upper()}")
    else:
        print(f"The closest alpha-numeric character is: {char.lower()}")
elif char.isdigit():
    print(f"The closest alpha-numeric character is: {char}")
else:
    print("Invalid input! Please enter a single character.")
    
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
r = 0.04

down_payment = portion_down_payment * total_cost
monthly_salary = annual_salary / 12
monthly_r = r / 12

current_savings = 0.0
months = 0

while current_savings < down_payment:
    current_savings += (portion_saved * monthly_salary) + (current_savings * monthly_r)
    months += 1

print("Number of months:", months)
