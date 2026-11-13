# Reverse an Array.

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


numbers = [10, 20, 30, 40, 50]

print("Original array:", numbers)

reverse_array(numbers)

print("Reversed array:", numbers)