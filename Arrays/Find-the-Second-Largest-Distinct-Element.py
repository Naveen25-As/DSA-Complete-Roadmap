# Find the Second Largest Distinct Element.

def find_second_largest(arr):
    largest = float("-inf")
    second_largest = float("-inf")

    for num in arr:

        if num > largest:
            second_largest = largest
            largest = num

        elif largest > num > second_largest:
            second_largest = num

    if second_largest == float("-inf"):
        return None

    return second_largest


numbers = [10, 25, 45, 30, 45, 20]

result = find_second_largest(numbers)

if result is None:
    print("Second largest element does not exist")
else:
    print("Second largest element:", result)