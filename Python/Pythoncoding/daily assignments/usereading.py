file_name = input("Please enter the file name: ")

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")