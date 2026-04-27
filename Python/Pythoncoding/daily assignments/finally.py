file_name = input("Enter the file name to open: ")

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

finally:
    print("Program execution completed.")