numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index to access an element from the list (0-4): "))

    # Access the element at the specified index
    element = numbers[index]
    print(f"The element at index {index} is: {element}")

except IndexError:
    print("Error: The index you entered is out of range.")
except ValueError:
    print("Error: Please enter a valid integer.")
