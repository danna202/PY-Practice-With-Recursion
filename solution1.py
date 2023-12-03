def print_numbers_down_to_zero(n):
    if n <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(n, -1, -1):
            print(i)

# Example usage:
positive_number = int(input("Enter a positive number: "))
print_numbers_down_to_zero(positive_number)
# Write code for algorithm 1 below