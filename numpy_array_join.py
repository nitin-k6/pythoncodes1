import numpy as np
arr1=np.array([12,32,41,16,85])
arr2=np.array([23,33,63,47,99])
arr=np.concatenate((arr1,arr2))
print(arr)

arr1=np.array([[11,10,173],[14,1500,161]])
arr2=np.array([[21,13,11],[312,35,3006]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)

