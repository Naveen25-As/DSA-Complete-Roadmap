# Longest Substring Without Repeating Characters.

def longest_substring(text):
    last_seen = {}

    left = 0
    maximum_length = 0

    for right in range(len(text)):

        char = text[right]

        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right

        current_length = right - left + 1

        maximum_length = max(maximum_length, current_length)

    return maximum_length


text = "abcabcbb"

result = longest_substring(text)

print("Original string:", text)
print("Longest substring length:", result)