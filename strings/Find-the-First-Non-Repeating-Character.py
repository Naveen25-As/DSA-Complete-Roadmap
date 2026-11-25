# Find the First Non-Repeating Character.

def first_non_repeating(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:

        if frequency[char] == 1:
            return char

    return None


text = "swiss"

result = first_non_repeating(text)

if result is not None:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")