# Check Armstrong Number.

def is_armstrong(number):
    if number < 0:
        return False

    original = number
    digits = len(str(number))
    total = 0
    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10
    return total == original


number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong Number")
else:
    print(number, "is Not an Armstrong Number")