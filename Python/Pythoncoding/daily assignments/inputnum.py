user_input = input("Please enter a number: ")

try:
    number = int(user_input)
    print(f"The integer is: {number}")
except ValueError:
    print("Error: That's not a valid number!")