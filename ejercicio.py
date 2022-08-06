# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

### <a name='0'></a> Import of libraries

np.__version__

### <a name='1'></a> Exercise 1
#Check if all array elements $ A, B, C $ and $ D $ return the logical value _True_.

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])


#__Tip:__ Use the function _np.all()_.

np.all(A)
np.all(B)
np.all(C)
np.all(D)

### <a name='2'></a> Exercise 2
# Check if all array elements $ A, B $ and $ C $ return the logical value _True_ along the axis with index 1.


A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])


#__Tip:__ Use the function _np.all()_ with the parameter _axis_.

np.any(A, axis=(-1))
np.any(B, axis=(-1))
np.any(C, axis=(-1))
np.any(D, axis=(-1))

# <a name='3'></a> Exercise 3
# Check if any element of arrays $ A, B, C $ and $ D $ returns the logical value _True_.


A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])


# __Tip:__ Use the _np.any()_ function.

np.any(A)
np.any(B)
np.any(C)
np.any(D)

# <a name='4'></a> Exercise 4
# Check if any element of arrays $ A, B, C $ and $ D $ returns the logical value _True_ along the axis with index 0.


A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])


# __Tip:__ Use the _np.any()_ function with the parameter _axis_.


np.any(A, axis=(0))
np.any(B, axis=(0))
np.any(C, axis=(0))
np.any(D, axis=(0))

# <a name='5'></a> Exercise 5
# Check the array $ A $ for missing data (_np.nan_).


A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])

# _Tip:__ Use the _np.isnan()_ function.
# enter solution here
np.isnan(A)

#  <a name='6'></a> Exercise 6
# if the following arrays $ A $ and $ B $ are equal in terms of elements (element-wise) with the specified tolerance level. Use the _np.allclose()_ function with default parameters.


A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])


# enter solution here
np.allclose(A, B)

# <a name='7'></a> Exercise 7
# Check if the following arrays $ A $ and $ B $ are equal in terms of elements (element-wise). Use the comparison operator _==_.


A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])


# enter solution here
A==B

# <a name='8'></a> Exercise 8

# Check which elements (element-wise) from the array $ A $ below have higher values than the array $ B $.


A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])


# enter solution here
np.greater(A,B)
                

# <a name='9'></a> Exercise 9

#  Create an array of numpy dimensions _4x4_ filled with zeros. Set the data type to _int_.

# __Expected result:__


array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]])

# __Tip:__ Use the _np.zeros()_ function.

# enter solution here
np.zeros((4,4))

# <a name='10'></a> Exercise 10
# Create an array of numpy dimensions _10x10_ filled with number 255. Set the data type to _float_.

# __Expected result:__

array([[255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.],
       [255., 255., 255., 255., 255., 255., 255., 255., 255., 255.]])


# __Tip:__ Use the _np.ones()_ or _np.full()_ functions.

# enter solution here
np.full((10,10),255.)

