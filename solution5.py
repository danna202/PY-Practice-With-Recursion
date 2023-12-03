# Write code for algorithm 5 below

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(s.split()).lower()

    # Compare the original string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage:
input_string = input("Enter a string: ")
result = is_palindrome(input_string)

print(f"The string '{input_string}' is a palindrome: {result}")

