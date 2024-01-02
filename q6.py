def is_palindrome(s):
    reversed_string = ''.join(reversed(s))
    return s == reversed_string

# Test the function
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f"{input_string} is a palindrome")
else:
    print(f"{input_string} is not a palindrome")
