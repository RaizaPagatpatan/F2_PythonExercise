#Number 1
# celsius = float(input("Enter temperature in Celsius: "))
#
# # Convert C to F
# fahrenheit = (celsius * 9/5) + 32
#
# decimal_part = int((fahrenheit - int(fahrenheit)) * 100)
#
# # Round off
# if decimal_part >= 50:
#     fahrenheit = int(fahrenheit) + 1
# fahrenheit = float(fahrenheit)
#
# print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")

#Number 2
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
# num3 = int(input("Enter the third integer: "))
#
# maximum = num1
#
# if num2 > maximum:
#     maximum = num2
#
# if num3 > maximum:
#     maximum = num3
#
# print(f"The maximum among {num1}, {num2}, and {num3} is: {maximum}")

#Number 3

num = int(input("Please enter a number: "))

count = 0
smallest = 9
highest = 0


if num == 0:
    count = 1
    smallest = 0
    highest = 0

while num != 0:
    digit = num % 10
    count += 1

    smallest = min(smallest, digit)
    highest = max(highest, digit)

    num //= 10


print(f"Number of digits in the given number is: {count}")
print(f"Smallest number is: {smallest}")
print(f"Highest number is: {highest}")
