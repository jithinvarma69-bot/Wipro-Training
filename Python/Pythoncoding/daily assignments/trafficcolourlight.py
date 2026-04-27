color = input("Enter the traffic light color (Red, Yellow, Green): ").capitalize()

match color:
    case 'Red':
        print("Stop!")
    case 'Yellow':
        print("Wait!")
    case 'Green':
        print("Go!")
    case _:
        print("Invalid color entered.")