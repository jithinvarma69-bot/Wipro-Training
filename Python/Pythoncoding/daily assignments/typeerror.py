def add_numbers(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None

print("Sum:", add_numbers(10, 5))
print("Sum:", add_numbers(10, "five"))