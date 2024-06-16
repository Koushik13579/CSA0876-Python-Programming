import numpy as np
matrix=[[1,2,3],
        [4,1,6],
        [7,8,1]]
mat=np.array(matrix)
invermat=np.linalg.inv(mat)
print("Inversion of matrix is :\n",invermat)