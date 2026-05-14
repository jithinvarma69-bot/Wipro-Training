import numpy as np

# Creating Arrays from Lists
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array from list:", array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array from list of lists:\n", array_2d)

# Array Attributes
print("Shape of array_2d:", array_2d.shape)
print("Size of array_2d:", array_2d.size)
print("Data type of array_2d:", array_2d.dtype)

array_float = np.array([1, 2, 3], dtype=np.float16)
print("Array with specified data type:", array_float)
print("Data type of array_float:", array_float.dtype)

# Built-in Functions
array_arange = np.arange(0.5, 10.75, 0.75)
print("Array with arange:", array_arange)

array_linspace = np.linspace(21, 51, 5)
print("Array with linspace:", array_linspace)

array_ones = np.ones((2, 3))
print("Array of ones:\n", array_ones)

array_zeros = np.zeros((2, 3))
print("Array of zeros:\n", array_zeros)

# Random Arrays
array_rand = np.random.rand(2, 3)
print("Random array with rand:\n", array_rand)

array_randn = np.random.randn(2, 3)
print("Random array with randn:\n", array_randn)

array_randint = np.random.randint(0, 10, (2, 3))
print("Random array with randint:\n", array_randint)

# Indexing and Slicing
array = np.array([[1, 2, 3], [4, 5, 6]])
print("Element at [0, 1]:", array[0, 1])
print("First row:", array[0, :])
print("First column:", array[:, 0])
print("Sub-array:", array[0:2, 1:3])

# Reshaping Arrays
array = np.arange(6)
print("Original array:", array)
print("Shape of array:", array.shape)

reshaped_array = array.reshape((2, 3))
print("Reshaped array:\n", reshaped_array)