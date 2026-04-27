while True:
    try:
        user_input = int(input("Please enter an integer: "))
        print(f"You entered the integer: {user_input}")
        break
    except ValueError:
        print("That's not a valid integer. Please try again.")