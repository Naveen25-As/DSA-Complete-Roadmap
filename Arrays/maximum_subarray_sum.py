# Maximum Subarray Sum Using Kadane's Algorithm.

def maximum_subarray_sum(arr):
    if not arr:
        raise ValueError("Array cannot be empty")

    current_sum = arr[0]
    maximum_sum = arr[0]

    for i in range(1, len(arr)):

        current_sum = max(arr[i], current_sum + arr[i])

        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = maximum_subarray_sum(numbers)

print("Maximum subarray sum:", result)