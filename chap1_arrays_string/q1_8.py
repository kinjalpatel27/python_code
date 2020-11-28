import numpy as np 

def method1(mat):
    mat = np.array(mat)
    def find_zero(mat):
        m, n = np.shape(mat)
        row = np.zeros(m)
        col = np.zeros(n)

        for i in range(m):
            for j in range(n):
                if mat[i,j]==0:
                    row[i] = 1
                    col[j] = 1
        return row, col


    def replace_zero_rc(mat, row, col):
        
        m,n = np.shape(mat)
        for i in range(m):
            if row[i] == 1:
                mat[i, :] = 0    
            
        for i in range(n):
            if col[i] == 1:
                mat[:, i] = 0    

        return mat
    row,col = find_zero(mat)
    mat = replace_zero_rc(mat,row,col)
    return mat

def method2(mat):
    mat = np.array(mat)
    m,n = np.shape(mat)
    
    #check first row and find if it has any zero
    rowzero = 0
    for j in range(n):
        if mat[0,j] == 0:
            rowzero = 1
            break
    #check first col and find if it has any zero
    colzero = 0
    for i in range(m):
        if mat[i, 0] == 0:
            colzero = 1
            break

    # set first row and column element to zero if
    # there is any zero in the particular row and column
    for i in range(m):
        for j in range(n):
            if mat[i,j] == 0:
                mat[0, j] = 0
                mat[i, 0] = 0

    # for each zero in row 0, set the column to 0
    for j in range(n):
        if mat[0,j] == 0:
            mat[:,j] = 0

    # for each zero in col 0, set the row to 0
    for i in range(m):
        if mat[i,0] == 0:
            mat[i,:] = 0
    
    if rowzero:
        mat[0,:] = 0
    if colzero:
        mat[:,0] = 0
    return mat

mat = np.random.randint(0,10,size=[6,6])
print("Before matrix ", mat)
mat1 = method1(mat)
print("After matrix ", mat1)

mat2 = method2(mat)
print("After matrix ", mat2)
assert (mat1 == mat2).any()
