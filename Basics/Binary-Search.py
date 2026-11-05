# Binary Search.

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50

index = binary_search(numbers, target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")