# Find the Factorial of a Number.

def factorial(number):
    if number < 0:
        return None

    result = 1

    for i in range(2, number + 1):
        result *= i

    return result


number = int(input("Enter a non-negative integer: "))

result = factorial(number)

if result is None:
    print("Factorial is not defined for negative integers.")
else:
    print("Factorial:", result)