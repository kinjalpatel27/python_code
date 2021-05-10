def insert(i, j, M, N):
    allones = ~0
    left = allones << i
    right = allones << j
    mask = left | right
    return (M & mask) | (N << i)


M = int("1000000000", 2)
N = int("10011", 2)
i = 2
j = 6
update_M = insert(i, j, M, N)
print(bin(update_M))
