# error detection during execution  is called exceptions.
# most exceptions are not handled by program and shows an error message.
'''
a = 10
b = 0
print(a/b)
ZeroDivisionError: division by zero
'''

# TRY, EXCEPT AND FINALLY STATEMENT:
  # TRY  block lets you test a block of code for errors.
  # except block lets you handle the error.
  # finally block lets you execute code , regardless of the result of the try- and except blocks.


  # EXCEPTION HANDLING:
     # using TRY statement:
         # try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("an exception occured")
    # output: an exception occured
    # try block raises an error, the except block will be executed.
    # without try block, the program will crash and raise an error.
#print(x) # output: NameError: name 'x' is not defined

# MANY EXCEPTIONS:
   # IF you want to execute a special block of code for a special kind of error:
    # print one message if the try block raises a Nameerror and another for other errors.
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something else went wrong")
    # variable x is not defined.

  # ELSE:
    # you can use the 'else'  keyword to define a block of code  to be executed if no errors were raised:
    # in this example , the try block does not generate any error:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("NOthing went wrong") # output : nothing went wrong


    # Finally:
      # the finally block will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished") # output: something went wrong
                                                    # the 'try except' is finished



    # Raise an exception:
      # to throw (or raise ) an exception, use the raise keyword.
     # eg: raise an error and stop the program if x is lower than 0:
'''
x = -1
if x < 0:
 raise Exception("Sorry, no numbers below zero")
'''

'''
output:
raise Exception("Sorry, no numbers below zero")
Exception: Sorry, no numbers below zero
'''


# NumPy module:
  # NumPy is a python library used for working with arrays.
  # NumPy was created in 2005 by Travis Oliphant.
  # it is an open source project and you can use it freely.
  # NumPy stands for Numerical Python.

  # NumPy creating Arrays:
    # array object in NumPy is called ndarray.
    # we can create a Numpy ndarray object by using the array() function.
    # eg:
import numpy
arr = numpy.array([1,2,3,4,5])
print(arr)
print(type(arr))
# [1 2 3 4 5]
# <class 'numpy.ndarray'>


  # to create an ndarray, we can pass a list, tuple or any array-like object into the array() method , and it will be converted into an ndarray:
   # use tuple to create a NumPy array:
import numpy as np
arr = np.array([1,2,"jhola", "jhanda"])
print(arr)
print(type(arr))
# ouput:
#['1' '2' 'jhola' 'jhanda']
#<class 'numpy.ndarray'>


# DIMENSIONS IN ARRAYS:
  # zero DIMENSION ARRAY OR  scalars, each value in an array is an 0-D array.
    # arr= np.array(43) # 0-d have only one value.

  #1-D array:
    # its elements are 0-d array.
      # arr= np.array([1,2,3,4,5,])

  #2-D array:
     # its elements are 1-d array.
      # arr = np.array([[1,2,3], [4,5,6]])
  # 3-D array:
    # its elements are 2-D matrices .
    # arr = np.array([[[1,2,3], [4,5,6]], [[1,4,5], [4,2,1]]])


  # CHECK HOW MANY DIMENSIONS ARRAY HAVE:
import numpy as np
a = np.array((45))
print(a.ndim) # output: 0
b = np.array([1,2,3,4])
print(b.ndim) # output: 1
c = np.array([[1,2],[3,4]])
print(c.ndim) # output: 2
d = np.array([[[2,4],[3,2]],[[4,3],[2,5]]])
print(d.ndim) # output: 3

# NumPy Array indexing and Accessing:
  # you can access an array element by referring to its index number.
   # indexes in NumPy arrays start with 0, first element has index 0, and the second has index 1 etc.
   # Eg: get the first element from the following array;
import numpy as np
arr = np.array([1,2,3,4])
print(arr[0]) # output: 1
print(arr[-1]) # output: 4

   # accessing 2-d and 3-d arrays.
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("0th element on 1st dim:", arr[0,0]) # output : 1
# arr[0,0] here initial 0 is 0th array which is 1,2,3,4,5 and next 0 in array shows index no. of the element
print("0th element on 2nd dim:", arr[1,0]) # output: 6, array first , index no.0 ,
print("1st element on 2nd dim:", arr[1,1]) # output: 7
print("2nd elemnt on 2nd dim", arr[1,2]) # output: 8
print(arr[1,-2]) # output: 9
print(arr[1,-5]) # output : 6

  # access the third element of the second array of the first array:
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,2]) # output: 6, 0 array which has 1,2,3,4,5,6, 0's 1st array which is 4,5,6. ;it's  2 index element: which is 6.
print(arr[1,1,2]) # output: 12.

# NumPy Array Slicing:
 # slicing in python means taking elements from one given index to another given index.
 # we pass slice instead of index like this: [start:end]
 # we can also define the step, like this: [start: end : step]
 # if we don't pass the start it is considered 0
 # if we don't pass end its considered length of array in that dimension
 # if we don't pass step it is considered 1
 # Eg: slice elements from index 1 to index 5 from the following array:
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5]) # output: [2 3 4 5], 1 is start and 5 is end. 5th element not included here we have printed element 1 to 5 not 5th.
print(arr[3:5]) # output: [4 5]
print(arr[0:-1]) # output: [1 2 3 4 5 6]
# slice the element from index 4 to end of the array:
arr = np.array([1,2,3,4,5,6,7])
print(arr[4:]) # output: [5 6 7]
# slice the element from the beginning to index 4(not included):
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[:4]) # output: [1 2 3 4]

# STEP:
  # use the step value to determine the step of the slicing:
  # Eg: return every other element from index 1 to index 5:
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5:2]) #output: [2 4]
print(arr[1:5:1]) #output:[2 3 4 5]
#print(arr[1:5:0]) # output: ValueError: slice step cannot be zero
print(arr[1:5:3]) # output:[2 5]
print(arr[1:5:4]) # output: [2]
print(arr[1:5:5]) # output: [2]
print(arr[1:5:6]) # output: [2]
print(arr[1:5:7]) # output:[2]

# return every other element from the entire array:
import numpy as np
arr = np.array([1,2,3,4,5,6,7])
print(arr[::2]) # output : [1 3 5 7]
print(arr[::3]) # output: [1 4 7]
print(arr[::4]) # output: [1 5]
print(arr[::5]) # output: [1 6]
print(arr[::6]) # output: [1 7]
print(arr[::7])# output: [1]
print(arr[::8]) # output: [1]
print(arr[::19]) # output: [1]


# PYthon CoPY:
  # the copy owns the data and any chages made to the copy will not affect original array
  # any change made to the original array will not affect the copy.
  # eg: make a copy , change the original array, and display both arrays:
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42
print(arr) # output: [42  2  3  4  5]
print(x) # output: [1 2 3 4 5]

#
import numpy as np
arr = np.array([1,2,3,4,5])
arr[0] = 42
x = arr.copy()
print(arr) # output: [42  2  3  4  5]
print(x) # output: [42 2 3 4 5]


# PYTHON VIEW:
  # view does not own the data  and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.
  # Eg: make a view and change the original array, and display both arrays:
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 54
print(arr) # output: [54  2  3  4  5]
print(x) # output: [54  2  3  4  5]
#
import numpy as np
arr = np.array([1,2,3,4,5])
arr[0] = 54
x = arr.view()
print(arr) # output: [54  2  3  4  5]
print(x) # output: [54  2  3  4  5]

# make a view , change the view and display both arrays:
import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
x[0] = 31
print(arr)# output: [31  2  3  4  5]
print(x) # output: [31  2  3  4  5]

# NumPy array iterating:
  # iterating means going through elements one by one.
  # as we deal with multi-dimensional array in numpy, we can do this using basic for loop of python.
  # Eg: iterate on the elements of the following 1-D array:
import numpy as np
arr = np.array([1,2,3])
for x in arr:
    print(x) # output: 1
                      #2
                      #3


    # NumPy joining Array:
      # joining means putting contents of two or more arrays in a single array.
      # we pass a sequence of arrays that we want to join to the concatenate() function, along with the axis.
      # if the axis is not explicitly passed , it is taken as 0.
    # Eg:
      # join two arrays:
import numpy as np
arr1 = np.array([1,2,3])
arr2= np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print(arr) # output: [1 2 3 4 5 6]


  # NumPy Splitting Array:
    # splitting is reverse operation of joining.
    # splitting breaks one into multiple.
    # we use array_split() for splitting arrays, we pass it the array we want to split and the no.of splits.
    # Eg: split the array in 3 parts:
import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3) # arr = name of variable , 3 is the no. of split to be done.
print(newarr) # output: [array([1, 2]), array([3, 4]), array([5, 6])]
newarr = np.array_split(arr,5)
print(newarr) #output: [array([1, 2]), array([3]), array([4]), array([5]), array([6])]


# NumPy searching arrays:
  # you can search an array for a certain value and return the indexes that get a match.
  # to search an array, use the 'where()'  method.
  # Eg: find the indexes where the value is 4:
import numpy as np
arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr==4)
print(x) # output: (array([3, 5, 6], dtype=int64),)
  #find the indexex where values are even:
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr%2==0)
print(x) #output: (array([1, 3, 5, 7], dtype=int64),), here 1,3,5,7 are index no.
# find the indexes where values are odd:
x = np.where (arr%2!= 0)
print(x) # output: (array([0, 2, 4, 6], dtype=int64),)
# another way: find odd values:
x = np.where (arr%2== 1)
print(x) #output: (array([0, 2, 4, 6], dtype=int64),)



# SEARCHSORT:
  # searchsort() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
  # searchsort() method is assumed to be used on sorted arrays.
  # Eg: find the indexes where the value 7 should be inserted:
import numpy as np
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,7)# arr variable name, 7 no. which to be find in array.
print(x) #output: 1
x = np.searchsorted(arr,9) # arr variable name, 9 no. which to be find in array.
print(x) # output: 3

  # search from the right side:
    # by default left most index is returned , but we can give side='right' to return the right most index instead.
    # Eg: fing the values where the value 7 should be inserted , starting from the right:
import numpy as np
arr = np.array([6,7,8,9])
x = np.searchsorted(arr,9,side='right')
print(x) #output: 4
x = np.searchsorted(arr,8,side='right')
print(x)# output: 3
x = np.searchsorted(arr,7,side='right')
print(x)# output:2
x = np.searchsorted(arr,6,side='right')
print(x)# output:1




# NumPy Sorting arrays:
  # sorting means putting elements in an ordered sequence.
  # ordered sequence = order corresponding to elemens, like numeric or alphabetical, ascending or descending.
  # the numpy ndarray object has a function called sort(), that will sort a specified array.
  # Eg: sort the array:
import numpy as np
arr = np.array([8,5,9,4])
print(np.sort(arr)) # output: [4 5 8 9]
# this method returns a copy of the array, leaving the original array unchanged.

# you can also sort arrays of strings , or any other data type:
# Eg: sort the array alphabetically:
import numpy as np
arr = np.array(['banana','cherry', 'apple'])
print(np.sort(arr)) # output: ['apple' 'banana' 'cherry']
# to reverse the order; in descending order:

import numpy as np
arr = np.array([8,5,9,4])

array_copy=np.sort(arr)[::-1] # output: [4 5 8 9]
print(array_copy) # output: [9 8 5 4]










