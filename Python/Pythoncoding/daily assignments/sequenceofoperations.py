
fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes']
print("Original List:", fruits)


fruits.append('Pineapple')
fruits.append('Peach')
fruits.remove('Mango')
print("Updated List:", fruits)


second_fruit = fruits[1]
fourth_fruit = fruits[3]
print("Second fruit:", second_fruit)
print("Fourth fruit:", fourth_fruit)


first_three_fruits = fruits[:3]
print("First three fruits:", first_three_fruits)


list_length = len(fruits)
print("Length of the list:", list_length)