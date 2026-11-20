# Reverse a String

def reverse_string(text):
    result = ""

    for char in text:
        result = char + result

    return result


text = input("Enter a string: ")
result = reverse_string(text)

print("Original string:", text)
print("Reversed string:", result)