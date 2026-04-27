text_to_append = "This is a new line added to the log."

with open("log.txt", "a") as log_file:
    log_file.write(text_to_append + "\n")

with open("log.txt", "r") as log_file:
    content = log_file.read()
    print("Contents of 'log.txt':")
    print(content)