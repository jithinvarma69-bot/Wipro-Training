
personal_info = {
    'name': 'John',
    'age': 25,
    'favorite_hobby': 'Reading'
}
print("Original Dictionary:", personal_info)


name_value = personal_info['name']
print("Name in the Dictionary:", name_value)


personal_info['favorite_food'] = 'Pizza'
personal_info['favorite_hobby'] = 'Cycling'
print("Updated Dictionary:", personal_info)


keys = personal_info.keys()
values = personal_info.values()
print("All Keys:", keys)
print("All Values:", values)


personal_info.pop('age')  # Removes the 'age' entry
print("Dictionary after removing 'age':", personal_info)