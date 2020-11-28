import numpy as np


def rotate(arry, N):
    assert np.shape(arry)[0] == np.shape(arry)[1]
    assert len(np.shape(arry)) == 2
    arry2 = np.zeros(np.shape(arry),dtype=np.int8)
    for i in range(N//2):
        arry2[i:N-i,N-i-1] = arry[i,i:N-i]
        arry2[N-i-1,i:N-i] = np.flip(arry[i:N-i,N-i-1])
        arry2[i:N-i,i] = arry[N-i-1, i:N-i]
        arry2[i,i:N-i] = np.flip(arry[i:N-i,i])
    if N%2 == 1:
        arry2[N//2,N//2] = arry[N//2,N//2]
    return arry2

def rotate_v1(arr):
    assert np.shape(arr)[0] == np.shape(arr)[1]
    assert len(np.shape(arr)) == 2
    n = np.shape(arr)[0]
    for i in range(n//2):
        for j in range(n-2*i-1):
            l_idx = n-i-1
            s_idx = i
            tmp = arr[j, l_idx]
            arr[j, l_idx] = arr[s_idx, j]
            arr[s_idx, j] = arr[l_idx-j, s_idx]
            arr[l_idx-j, s_idx] = arr[l_idx, l_idx-j]
            arr[l_idx, l_idx-j] = tmp
    return arr

N = 4
arr1 = np.random.randint(10,size=(N,N))
assert (np.rot90(arr1,axes=(1,0)) == rotate(arr1,N)).any()
assert (np.rot90(arr1,axes=(1,0)) == rotate_v1(arr1)).any()

N = 3
arr1 = np.random.randint(10,size=(N,N))
assert (np.rot90(arr1,axes=(1,0)) == rotate(arr1,N)).any()
assert (np.rot90(arr1,axes=(1,0)) == rotate_v1(arr1)).any()
