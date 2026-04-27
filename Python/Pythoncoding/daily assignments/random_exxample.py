import random

random_integer = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_integer}")

random_numbers = [random.randint(1, 50) for _ in range(10)]
print(f"List of random numbers: {random_numbers}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(f"Shuffled list of numbers: {numbers}")