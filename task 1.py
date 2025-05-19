def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Sample number
sample_number = 5
# Calling the function and printing the output
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")
