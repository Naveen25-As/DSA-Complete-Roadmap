# Check Palindrome Number

def is_palindrome(number):
    if number < 0:
        return False

    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original == reversed_number


number = int(input("Enter a number: "))

if is_palindrome(number):
    print(number, "is a Palindrome")
else:
    print(number, "is Not a Palindrome")