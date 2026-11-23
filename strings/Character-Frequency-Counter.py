# Character Frequency Counter.

def character_frequency(text):
    frequency = {}

    for char in text:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


text = "programming"

result = character_frequency(text)

print("Character frequencies:")

for char, count in result.items():
    print(char, ":", count)