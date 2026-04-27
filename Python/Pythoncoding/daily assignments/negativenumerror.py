class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass


try:
    number = float(input("Please enter a positive number: "))

    if number < 0:
        raise NegativeNumberError("You entered a negative number, which is not allowed.")

    print(f"You entered a positive number: {number}")

except NegativeNumberError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid number.")