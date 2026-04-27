try:
    with open("source.txt", "r") as source_file:
        content = source_file.read()

    with open("destination.txt", "w") as destination_file:
        destination_file.write(content)

    print("Contents of 'source.txt' have been written to 'destination.txt'.")

except FileNotFoundError:
    print("Error: 'source.txt' not found. Please ensure the file exists.")