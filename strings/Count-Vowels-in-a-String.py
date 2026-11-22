# Count Vowels in a String.

def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():

        if char in vowels:
            count += 1

    return count


text = "Python Programming"

result = count_vowels(text)

print("String:", text)
print("Number of vowels:", result)