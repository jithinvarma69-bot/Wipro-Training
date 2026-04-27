text = input("Enter some text: ")

with open("output.txt", "w") as file:
    file.write(text)

with open("output.txt", "r") as file:
    content = file.read()
    print(content)