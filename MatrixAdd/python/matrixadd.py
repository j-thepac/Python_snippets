"""
Write a function that accepts two square matrices (N x N two dimensional arrays), and return the sum of the two. Both matrices being passed into the function will be of size N x N (square), containing only integers.

How to sum two matrices:

Take each cell [n][m] from the first matrix, and add it with the same [n][m] cell from the second matrix. This will be cell [n][m] of the solution matrix. (Except for C where solution matrix will be a 1d pseudo-multidimensional array).

Visualization:

|1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
|3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
|1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|
"""
import numpy as np 
def matrix_addition(a,b):
    fx=np.vectorize(lambda x: int(x))
    a_np=np.array(a)
    b_np=np.array(b)
    return (fx(a_np)+fx(b_np)).tolist()

def matrix_addition2(a,b):
    res=[]
    for row in range(0,len(a)):
        res2=[]
        for col in range(0,len(a[0])):
            res2.append(a[row][col]+b[row][col])
        res.append(res2)
    return res


assert(matrix_addition(
  [[1, 2],[1, 2]],

  [[2, 3],[2, 3] ])==
#     =
  [ [3, 5],[3, 5] ] )

assert(matrix_addition(
  [ [1] ],
#    +
  [ [2] ] )==
#    =
  [ [3] ] )

assert(matrix_addition(
  [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
#       +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] )==
#       =
  [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ] )


print("done")