
celsius = float(input("Enter temperature in Celsius: "))

# Convert C to F
fahrenheit = (celsius * 9/5) + 32

decimal_part = int((fahrenheit - int(fahrenheit)) * 100)

# Round off
if decimal_part >= 50:
    fahrenheit = int(fahrenheit) + 1
fahrenheit = float(fahrenheit)

print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
