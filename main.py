#Raiza Pagatpatan F2

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

# num = int(input("Please enter a number: "))
#
# count = 0
# smallest = 9
# highest = 0
#
#
# if num == 0:
#     count = 1
#     smallest = 0
#     highest = 0
#
# while num != 0:
#     digit = num % 10
#     count += 1
#
#     smallest = min(smallest, digit)
#     highest = max(highest, digit)
#
#     num //= 10
#
#
# print(f"Number of digits in the given number is: {count}")
# print(f"Smallest number is: {smallest}")
# print(f"Highest number is: {highest}")

#Number 4
# n = int(input("Enter a number: "))
# total = 0
#
# for i in range(1, n + 1):
#     total += i
# print(f"The sum of numbers from 1 to {n} is: {total}")

#Number 5
# Dec-Binary
def decToBinary(dec):
    binary = ""
    if dec == 0:
        return "0"
    while dec > 0:
        binary = str(dec % 2) + binary
        dec //= 2
    return binary


# bi-dec, oct, dec, hex, dect
def binaryToN(bin_or_oct_or_hex, base):
    decimal = 0
    power = 0
    for digit in reversed(bin_or_oct_or_hex):
        if base == 2:
            decimal += int(digit) * (2 ** power)
        elif base == 8:
            decimal += int(digit) * (8 ** power)
        elif base == 16:
            decimal += int(digit, 16) * (16 ** power)
        power += 1
    return decimal


# Dec-Oct
def decToOctal(dec):
    octal = ""
    if dec == 0:
        return "0"
    while dec > 0:
        octal = str(dec % 8) + octal
        dec //= 8
    return octal


# Dec-Hex
def decToHex(dec):
    hexadecimal = ""
    if dec == 0:
        return "0"
    while dec > 0:
        remainder = dec % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        dec //= 16
    return hexadecimal



def main():
    decimal_input = int(input("Enter a decimal number: "))

    binary_result = decToBinary(decimal_input)
    octal_result = decToOctal(decimal_input)
    hexadecimal_result = decToHex(decimal_input)

    print(f"Decimal to Binary: {binary_result}")
    print(f"Decimal to Octal: {octal_result}")
    print(f"Decimal to Hexadecimal: {hexadecimal_result}")


if __name__ == "__main__":
    main()

