from asyncio import events
import numpy as np
arr=np.array([11,54,22,76,87,22,69,5,60,71,22])
x=np.where( arr == 22)
print(x)  #print the indexes where 22 is present

#  print where indexes are even
arrr=np.array([23,33,56,98,72,66,19])
x=np.where( arrr%2 == 0)
print(x)

# print where indexes are odd
arrrr=np.array([23,33,56,98,72,66,19])
x=np.where( arrrr%2 == 1)
print(x)

# Search sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
# The searchsorted() method is assumed to be used on sorted arrays.
import numpy as np
arr=np.array([12,16,22,34,55,62,86])
# x=np.searchsorted(arr,44)
x = np.searchsorted(arr, 16, side='right') #By default the left most index is returned, but we can give side='right' to return the right most index instead.
# The method starts the search from the right and returns the first index where the number 7 is no longer less than the next value.
print(x)

arr=np.array([11,13,14,15,18,21])
x=np.searchsorted(arr,[15,17,20])
print(x)