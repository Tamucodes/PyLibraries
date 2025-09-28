import numpy as np
import random 
a = np.array([[1,2,3],
             [2,3,4],
             [5,1,2]])

#initalization of different types of array
empty = np.zeros((3,3,3)) # enter the desired format of the null matrix.  
# print(empty)

#indentity matrix or 1's array
identity = np.ones((3,3))
# print(identity,identity.dtype)

#any other number thats repeated in the whole matrix
#format => np.full((n,m),number)
full = np.full((2,2),99) # here only 2 parameters are accepted.  
# print(full)


#full-like modification to an existing array of any order
fully = np.full_like(a,4) # here the number 4 is replaced in terms of each and every element present in the array a.
# format for the full_like is n {np.full_like(existing-array,the replacing element)}
# print(fully)    

#random decimal number
deci_random = np.random.rand(1,2) # no needed to apss tupels 
print(deci_random)

#random integer 