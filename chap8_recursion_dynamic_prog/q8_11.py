def coin_pairs(n, denom, idx=0):
    if n == 1 or denom[idx] == 1 or n == 0:
        return 1
    if n < 0 or idx >= len(denom):
        return 0

    count = 0
    num = 0
    while n >= (num) * denom[idx]:
        count += coin_pairs(n - num * denom[idx], denom, idx + 1)
        num += 1
    return count


denom = [25, 10, 5, 1]
print(coin_pairs(27, denom))
