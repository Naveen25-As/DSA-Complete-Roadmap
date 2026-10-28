# Find the Largest Element in an Array.

def find_largest(numbers):
    if not numbers:
        raise ValueError("The array must not be empty.")

    largest = numbers[0]

    for number in numbers[1:]:
        if number > largest:
            largest = number

    return largest


numbers = [12, 45, 7, 89, 23]

print("Array:", numbers)
print("Largest element:", find_largest(numbers))