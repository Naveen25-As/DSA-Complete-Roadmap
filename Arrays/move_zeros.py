# Move Zeros to the End of an Array.

def move_zeros(arr):
    position = 0

    for i in range(len(arr)):

        if arr[i] != 0:
            arr[position] = arr[i]
            position += 1

    while position < len(arr):
        arr[position] = 0
        position += 1

    return arr


numbers = [0, 1, 0, 3, 12, 0, 5]

print("Original array:", numbers)

move_zeros(numbers)

print("After moving zeros:", numbers)