# Remove Duplicates from an Array.


def remove_duplicates(arr):
    result = []
    seen = set()

    for num in arr:

        if num not in seen:
            result.append(num)
            seen.add(num)

    return result


numbers = [10, 20, 10, 30, 40, 20, 50, 30]

result = remove_duplicates(numbers)

print("Original array:", numbers)
print("Array after removing duplicates:", result)