grade = input("Enter your grade (A, B, C, D, F): ").upper()

match grade:
    case 'A':
        print("Excellent!")
    case 'B':
        print("Good!")
    case 'C':
        print("Average!")
    case 'D':
        print("Below Average!")
    case 'F':
        print("Fail!")
    case _:
        print("Invalid grade entered.")