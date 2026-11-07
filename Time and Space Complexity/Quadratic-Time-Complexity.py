#  Quadratic Time Complexity.

def display_pairs(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])


numbers = [1, 2, 3]

print("All Possible Pairs:")

display_pairs(numbers)