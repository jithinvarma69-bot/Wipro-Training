try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Convert the inputs to integers
    num1 = int(num1)
    num2 = int(num2)

    # Perform division
    result = num1 / num2
    print(f"The result of the division is: {result}")

except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")