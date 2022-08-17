# Checking number of dimension
import numpy as np
a=np.array(32)
b=np.array([1,2,3,4,5,6,7,8,9])
c=np.array([[1,2,3],[5,6,7,8]])
d=np.array([[[1,2,3,4],[5,6,7]],[[1,2,3,4],[5,6,7]]])

# NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


