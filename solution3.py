# Write code for algorithm 3 below
def fibonacci_recursive(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = int(input("Enter a positive integer (n): "))
result = fibonacci_recursive(n)
print(f"The {n}th element in the Fibonacci Sequence is: {result}")
