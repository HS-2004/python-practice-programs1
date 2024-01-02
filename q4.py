def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_armstrong(n):
    order = len(str(n))
    sum_val = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** order
        temp //= 10
    return n == sum_val

while True:
    print("\nMenu:")
    print("A. Check if the given number is a prime number.")
    print("B. Calculate Factorial of given number.")
    print("C. Check if the given number is palindrome or not.")
    print("D. Check if the given number is Armstrong number.")
    print("E. Exit")
    
    choice = input("Enter your choice (A, B, C, D, or E): ")

    if choice == 'A':
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
    elif choice == 'B':
        num = int(input("Enter a number: "))
        factorial = calculate_factorial(num)
        print("Factorial of", num, "is", factorial)
    elif choice == 'C':
        num = int(input("Enter a number: "))
        if is_palindrome(num):
            print(num, "is a palindrome")
        else:
            print(num, "is not a palindrome")
    elif choice == 'D':
        num = int(input("Enter a number: "))
        if is_armstrong(num):
            print(num, "is an Armstrong number")
        else:
            print(num, "is not an Armstrong number")
    elif choice == 'E':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter A, B, C, D, or E.")
# case sensitive 