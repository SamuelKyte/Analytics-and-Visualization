'''Create a new program named compTask1.py and add comments and code
to answers to the following questions:
=====================================================================

○ Why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float) 
create a two dimensional array? Write it the correct way.

Proper annotation for a 2D array is (np.array([[1, 0, 0], [0, 1, 0]], dtype=float)

If this is a 2D array, we can only have 2 arguements, not 3 within closed brackets. 
The dtype must be defined outside of the array brackets.


○ What is the difference between a = np.array([0, 0, 0]) and a =np.array([[0, 0, 0]])?

The first refers to a slice from a 1D array, the second refers to a slice from a 2D array.


○ A 3 by 4 by 4 is created with arr = np.linspace(1, 48,48).reshape(3, 4, 4). 
Index or slice this array to obtain the following:
■ 20.0
■ [ 9. 10. 11. 12.]
■ [[33. 34. 35. 36.] [37. 38. 39. 40.] [41. 42. 43. 44.] [45. 46. 47. 48.]]
■ [[5. 6.], [21. 22.] [37. 38.]]
■ [[36. 35.] [40. 39.] [44. 43.] [48. 47.]]
■ [[13. 9. 5. 1.] [29. 25. 21. 17.] [45. 41. 37. 33.]]
■ [[1. 4.] [45. 48.]]
■ [[25. 26. 27. 28.], [29. 30. 31. 32.], [33. 34. 35. 36.], [37. 38. 39. 40.]]
(Answers below)
'''
# Got help here: https://scipython.com/book/chapter-6-numpy/questions/indexing-and-slicing-a-numpy-array/

 #  import packages
import numpy as np 

 #  define array as arr, as detailed by task
arr = np.linspace(1, 48,48).reshape(3, 4, 4)

 #  print slices of array

 #  20.0
print(arr[1,0,3])

 #  [  9.  10.  11.  12.]
print(arr[0,2,:])

 #  [[ 33.  34.  35.  36.]
 #   [ 37.  38.  39.  40.]
 #   [ 41.  42.  43.  44.]
 #   [ 45.  46.  47.  48.]]
print(arr[2,...])

 #  [[  5.,   6.],
 #  [ 21.,  22.],
 #  [ 37.,  38.]]
print(arr[:,1,:2])

 #  [[ 36.  35.]
 #  [ 40.  39.]
 #  [ 44.  43.]
 #  [ 48.  47.]]
print(arr[2,:,:1:-1]) # in the third block, for each row take the items in the middle two columns

 #  [[ 13.   9.   5.   1.]
 #  [ 29.  25.  21.  17.]
 #  [ 45.  41.  37.  33.]]
print(arr[:,::-1,0]) #  for each block, traverse the rows backwards and take the item in the first column of each

 #  [[  1.   4.]
 #  [ 45.  48.]]
 #  create an array of indexes
 # three 2×2 index arrays for the blocks, rows and columns
ia = np.array([[0, 0], [2, 2]])
ja = np.array([[0, 0], [3, 3]])
ka = np.array([[0, 3], [0, 3]])

a = arr[ia,ja,ka] # print result
print(a)


# got help here: https://stackoverflow.com/questions/57600547/home-work-problem-that-i-cant-visualize-to-understand-python-numpy-newbie
mask_blocks = np.array([1,2])

x = arr[mask_blocks] #gets the columns

mask_rows = np.array([2,3]) #mask the rows

x = arr[mask_blocks][:, mask_rows] #index/slice the matrix

mask_index = np.array([0,3]) #mask for indexes

#arr[1][2:4,:] gets second block, last two rows
#arr[2][0:2,:] gets third block, first two rows

print(np.array([arr[1][2:4,:], arr[2][0:2,:]]).reshape(4,4).tolist()) #prints list