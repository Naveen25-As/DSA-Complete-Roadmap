# Find GCD and LCM of Two Numbers.

def find_gcd(a, b):
    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // find_gcd(a, b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD:", find_gcd(a, b))
print("LCM:", find_lcm(a, b))