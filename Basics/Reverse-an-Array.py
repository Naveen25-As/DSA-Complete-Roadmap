# Reverse an Array.

def reverse_array(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers


numbers = [10, 20, 30, 40, 50]

print("Original array:", numbers)
print("Reversed array:", reverse_array(numbers))