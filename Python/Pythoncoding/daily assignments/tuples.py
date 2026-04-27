
cities = ('Paris', 'Tokyo', 'New York')
print("Original Tuple:", cities)


first_city = cities[0]
last_city = cities[-1]
print("First city:", first_city)
print("Last city:", last_city)


more_cities = ('London', 'Sydney')
all_cities = cities + more_cities
print("Concatenated Tuple:", all_cities)


try:
    cities[1] = 'Berlin'  
except TypeError as e:
    print("Error:", e)


city1, city2, city3 = cities
print("Unpacked Cities:")
print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)