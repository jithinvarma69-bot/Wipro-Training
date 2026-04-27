numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(f"Largest number: {max(numbers)}")
print(f"Smallest number: {min(numbers)}")

string_input = input("Enter a string: ")
print(f"Length of the string: {len(string_input)}")

names = input("Enter a list of names separated by spaces: ").split()
names.sort()
print("Names in alphabetical order:", names)

numbers_for_sum = list(map(int, input("Enter another list of numbers separated by spaces: ").split()))
print(f"Total sum of the numbers: {sum(numbers_for_sum)}")

string_to_uppercase = input("Enter a string to convert to uppercase: ")
print(f"Uppercase string: {string_to_uppercase.upper()}")