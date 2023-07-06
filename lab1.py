def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

def is_palindrome(num):
    num = str(num)
    return num == num[::-1]

def count_digits(num):
    return len(str(num))

def process_number():
    number = int(input("Enter an integer: "))

    if number % 2 == 1:  # odd number
        fact = factorial(number)
        digit_count = count_digits(fact)
        print(f"The factorial of {number} is: {fact}")
        print(f"The number of digits in the factorial is: {digit_count}")
    else:  # even number
        if is_palindrome(number):
            print(f"The number {number} is a palindrome.")
        else:
            print(f"The number {number} is not a palindrome.")

process_number()
