
colors = {'Red', 'Blue', 'Green', 'Yellow', 'Purple'}
print("Original Set of Colors:", colors)


colors.add('Orange')
colors.remove('Yellow')
print("Updated Set of Colors:", colors)


more_colors = {'Pink', 'Cyan', 'Magenta'}


intersection = colors.intersection(more_colors)
union = colors.union(more_colors)
difference = colors.difference(more_colors)

print("Intersection of Sets:", intersection)
print("Union of Sets:", union)
print("Difference of Sets:", difference)


color_check = 'Red'
is_in_set = color_check in colors
print(f"Is '{color_check}' in the set? {is_in_set}")


fruits = ['Apple', 'Banana', 'Apple', 'Mango', 'Orange', 'Banana', 'Grapes']
unique_fruits = set(fruits)
print("Unique Fruits:", unique_fruits)