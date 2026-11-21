# Check Whether a String Is a Palindrome.


def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


text=input("Enter a text to check palindrome or Not:")
if is_palindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")