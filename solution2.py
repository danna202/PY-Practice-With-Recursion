def print_natural_numbers(n):
    if n < 1:
        print("Please enter a positive integer.")
    else:
        for i in range(1, n + 1):
            print(i)

# Example usage:
n = int(input("Enter a positive integer (n): "))
print_natural_numbers(n)
# Write code for algorithm 2 below