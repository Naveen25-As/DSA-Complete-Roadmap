# Find the Largest Element in an Array.

def find_largest(arr):
    if not arr:
        raise ValueError("Array cannot be empty")

    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest


numbers = [12, 45, 23, 67, 34, 89, 10]

result = find_largest(numbers)

print("Largest element:", result)