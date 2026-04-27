password = input("Enter your password: ")

if len(password) >= 8:
    print("Your password is strong.")
else:
    print("Your password is not strong. It must be at least 8 characters long.")