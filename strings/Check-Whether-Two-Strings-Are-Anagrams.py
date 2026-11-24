# Check Whether Two Strings Are Anagrams.

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    frequency = {}

    for char in str1:
        frequency[char] = frequency.get(char, 0) + 1

    for char in str2:

        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] < 0:
            return False

    return True


str1 = "listen"
str2 = "silent"

if are_anagrams(str1, str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")