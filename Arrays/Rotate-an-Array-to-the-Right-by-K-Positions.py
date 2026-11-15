#  Rotate an Array to the Right by K Positions.

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1


def rotate_array(arr, k):
    n = len(arr)

    if n == 0:
        return arr

    k = k % n

    if k == 0:
        return arr

    reverse(arr, 0, n - 1)
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)

    return arr


numbers = [1, 2, 3, 4, 5, 6, 7]

k = 3

print("Original array:", numbers)

rotate_array(numbers, k)

print("Rotated array:", numbers)