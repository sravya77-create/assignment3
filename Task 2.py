import math

# Asking the user for a number as input
user_input = float(input("Enter a number: "))

# Calculating the square root, natural logarithm, and sine
square_root = math.sqrt(user_input)
natural_log = math.log(user_input)
sine_value = math.sin(user_input)

# Displaying the calculated results
print(f"Square root of {user_input} is: {square_root}")
print(f"Natural logarithm (log base e) of {user_input} is: {natural_log}")
print(f"Sine of {user_input} (in radians) is: {sine_value}")
