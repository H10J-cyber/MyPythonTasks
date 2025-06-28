def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))
result = factorial(5)
print(result)


#task 2
import math

# Ask the user for a number
number = float(input("Enter a number: "))

# Calculate and print results directly using math module
print("\nCalculated results:")
print("Square root:", math.sqrt(number))
print("Natural logarithm:", math.log(number))
print("Sine (in radians):", math.sin(number))
print("Pi (for reference):", math.pi)