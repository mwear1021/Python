""" Exercise 1: Create a 4X2 integer array and Prints its attributes

note: The element must be a type of unsigned int16. And print the following Attributes: 
The shape of an array.
Array dimensions.
The Length of each element of the array in bytes.
 """
import numpy as np

first_array = np.empty([4,2], dtype=np.uint16)

print("\nPrinting array: \n")
print(first_array)

print("\nArray Dimensions: \n")
print("Array shape: ", first_array.shape)
print("Array dimensions: ", first_array.ndim)
print("length of each element of the array in bytes: ", first_array.itemsize)