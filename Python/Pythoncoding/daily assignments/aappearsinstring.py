# Example string
input_string = "banana"

# Using enumerate to count occurrences of 'a'
count_a = sum(1 for index, char in enumerate(input_string) if char == 'a')

print(count_a)