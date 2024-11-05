import ctypes

# Load the shared library (libarray.dylib for macOS, libarray.so for Linux)
lib = ctypes.CDLL('./libarray.dylib')

# Define the argument and return types of the sum_array function
lib.sum_array.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
lib.sum_array.restype = ctypes.c_int

# Define the input array and length
array = [1, 2, 3, 4, 5]
array_len = len(array)

# Convert the Python list to a ctypes array of integers
array_c = (ctypes.c_int * array_len)(*array)

# Call the C++ function
result = lib.sum_array(array_c, array_len)

# Print the result
print(f"Sum of the array: {result}")
