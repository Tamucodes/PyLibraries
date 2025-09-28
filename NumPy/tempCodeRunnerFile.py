import numpy as np 
import sys

# accessing/ changing the specific element, row, columns ets

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a[0,5]) # to get a speicific elemen array_name.[Row,column]

#to get a specific row/ columns
print(a[0,:])
print(a[:,1])

#Getting elements in a squence. Format => [startIndex:endIndex:stepSize]
print(a[1, 0:6:2])

#changing the elemnts in the array
a[1,4] = 21
print(a)