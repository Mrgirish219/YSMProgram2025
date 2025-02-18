# 1. Write a program to find the largest of two numbers using if-else statements.
a = 10
b = 20

if a > b:
    print("a is larger than b")
else:
    print("b is larger than or equal to a")
#2. Write a program that uses if-else statements to print whether a number is positive, negative, or zero.

num = -5

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

#3. Write a program that checks whether a given number is even or odd using the ternary operator.
num = 4
result = "Even" if num % 2 == 0 else "Odd"
print(result)

#4. What is the output of the following expression? result = 25 // 4 * 3 + 18 % 7 - 5 * 2 / 2
result = 25 // 4 * 3 + 18 % 7 - 5 * 2 / 2
print(result)  # Output is 16.0

#5. Write a program to calculate the area of a triangle given its base and height using the formula Area = (base * height) / 2.
base = 10
height = 5
area = (base * height) / 2
print("Area of the triangle:", area)


#6. Write a program to calculate the perimeter of a rectangle using length and width variables.
length = 7
width = 4
perimeter = 2 * (length + width)
print("Perimeter of the rectangle:", perimeter)

#7. Write a program that uses the modulus operator (%) to find the remainder when dividing two numbers
num1 = 10
num2 = 3
remainder = num1 % num2
print("Remainder:", remainder)

#8. Write a program to compare two numbers and print whether the first is greater, smaller, or equal to the second using relational operators.
a = 15
b = 20

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")

#9. Write a program that takes two integers and performs both floor division (//) and modulo (%) operations. Print the results
num1 = 25
num2 = 4

floor_division_result = num1 // num2
modulo_result = num1 % num2

print("Floor division result:", floor_division_result)
print("Modulo result:", modulo_result)

#10. Write a program that prints the grade based on the score input using if-else statements (A for 90-100, B for 80-89, etc.).
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
