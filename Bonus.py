def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print(f"The greatest common divisor of {num1} and {num2} is: {result}")
