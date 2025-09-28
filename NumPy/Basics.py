import numpy as np 
import sys

# Inserting varius multidimensional arrays
a = np.array([[1,2,3],
             [2,3,4],
             [5,1,2]]) #3X3 dimension
b = np.array([[1,2.01,3.44,4,5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20]]) # 4X5 dimension

#working with 3 dimensional arrays
d3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) 

#prints the size of array in each dimension
# for a matrix with n rows and m columns the shape would be (n,m)
print(a.shape) # dispalyed in cartsian form 
print(b.shape)

#number of dimensionas in an array
print(b.ndim)
print(a.ndim)

#total no of elements in that array
print(a.size)
print(b.size)

#the type of element inside of the array
print(a.dtype)
print(b.dtype)

#the size of each element in the array 
#for float64 has itemSize 8 and complez32 has itemSize 4
print(a.itemsize)
print(b.itemsize)


#printing the 3 dimensional array
print(d3[:,1,:])