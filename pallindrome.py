def is_palindrome(s):
    return s == s[::-1]

# Example
string = "madam"
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")