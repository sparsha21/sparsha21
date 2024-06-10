Q1
import numpy as np

# Create a random vector of size 15 with integers in the range 1-20
random_vector=np.random.randint(1,20,size=15)
print(random_vector)

# Reshape the array to 3 by 5
reshaped_array = random_vector.reshape(3, 5)
print("Array shape before replacing max values:")
print(reshaped_array.shape)

# Replace the max in each row by 0
max_indices = np.argmax(reshaped_array, axis=1)
for i in range(len(reshaped_array)):
   reshaped_array[i, max_indices[i]] = 0

# Print array shape after replacing max values
print("Array shape after replacing max values: ")
print(reshaped_array.shape)

# Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements)
array_2d = np.random.randint(low=-100, high=100, size=(4, 3),dtype=np.int32)
print( "Array shape:", array_2d.shape)
print("Array type:", type(array_2d))
print("Array data type:", array_2d.dtype)

Q2.
import numpy as np

array=np.array([[3,-2],[1,0]])

eigenvalues, eigenvectors = np.linalg.eig(array)

print("Eigenvalues:", eigenvalues)
print("Right Eigenvectors:\n", eigenvectors)

Q3.
import numpy as np

array=np.array([[0,1,2],[3,4,5]])

diagonal_sum = np.trace(array)

print("Sum of the diagonal elements:", diagonal_sum)

Q4.

import numpy as np

array1=np.array([[1,2],[3,4],[5,6]])
array2=np.array([[1,2,3],[4,5,6]])

reshaped_array1=np.reshape(array1,(2,3))
reshaped_array2=np.reshape(array2,(3,2))

print("Reshaped array1 (2*3):")
print(reshaped_array1)
print("Reshaped array2 (3*2):")
print(reshaped_array2)
