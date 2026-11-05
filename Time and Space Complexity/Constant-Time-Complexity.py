# Constant Time Complexity.

def get_first_element(numbers):
    if not numbers:
        return None

    return numbers[0]


numbers = [10, 20, 30, 40, 50]

result = get_first_element(numbers)

print("Array:", numbers)
print("First Element:", result)