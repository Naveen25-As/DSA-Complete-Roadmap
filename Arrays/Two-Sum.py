# Two Sum.

def two_sum(arr, target):
    seen = {}

    for i in range(len(arr)):

        required = target - arr[i]

        if required in seen:
            return [seen[required], i]

        seen[arr[i]] = i

    return []


numbers = [2, 7, 11, 15]

target = 9

result = two_sum(numbers, target)

if result:
    print("Indices:", result)
    print("Numbers:", numbers[result[0]], "and", numbers[result[1]])
else:
    print("No pair found")