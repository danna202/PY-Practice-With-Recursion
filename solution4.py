# Write code for algorithm 4 below
def power(a, b):
    result = a ** b
    return result

# Example usage:
base = float(input("Enter the base (a): "))
exponent = float(input("Enter the exponent (b): "))

result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
