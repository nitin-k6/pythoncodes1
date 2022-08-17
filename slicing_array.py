import numpy as np
arr=np.array([12,32,41,56,39,46,2,73])
print(arr[1:5]) #Slicing elements from index 1 to index 5.The result includes the start index, but excludes the end index.
print(arr[2:])   #Start from mentioned index.Slice elements from index 2 to the end of the array
print(arr[:3])  #Exclude the mentioned index.Slice elements from the beginning to index 4 (not included):

#Negative slicing
print(arr[-3:-1])  #Slice from the index 3 from the end to index 1 from the end.Exclude thelast mentioned index
