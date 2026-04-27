import os

def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()

def string_length(s):
    return len(s)

def is_palindrome(s):
    return s == s[::-1]

def is_alphabetic(s):
    return s.isalpha()

sample_string = "hello"
print(f"Original string: {sample_string}")
print(f"Reversed string: {reverse_string(sample_string)}")
print(f"Uppercase string: {to_uppercase(sample_string)}")
print(f"Length of string: {string_length(sample_string)}")

palindrome_string = "madam"
non_palindrome_string = "hello"

print(f"Is '{palindrome_string}' a palindrome? {is_palindrome(palindrome_string)}")
print(f"Is '{non_palindrome_string}' a palindrome? {is_palindrome(non_palindrome_string)}")

alphabetic_string = "hello"
non_alphabetic_string = "hello123"

print(f"Is '{alphabetic_string}' alphabetic? {is_alphabetic(alphabetic_string)}")
print(f"Is '{non_alphabetic_string}' alphabetic? {is_alphabetic(non_alphabetic_string)}")