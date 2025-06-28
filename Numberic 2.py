
print(max(1,2,3,4,5,6))
print(min(7,4,3,8,5,6))
#absolute value
print(abs(-2020))
#power
print(pow(2,3))
# Assignment
# Step 1: Take input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Division with check for zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"
# Step 3: Show results
print("Results:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
