# Logarithmic Time Complexity.

def logarithmic_example(number):
    steps = 0

    while number > 0:
        print("Current number:", number)

        number //= 2
        steps += 1

    return steps


number = int(input("Enter a positive number: "))

if number <= 0:
    print("Please enter a positive number.")
else:
    total_steps = logarithmic_example(number)

    print("Total Steps:", total_steps)