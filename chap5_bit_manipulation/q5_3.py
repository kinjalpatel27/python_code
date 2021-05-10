def flip_win(num):
    prev_len = 0
    curr_len = 0
    max_len = 0

    while num != 0:
        bit = num & 1
        if bit == 1:
            curr_len += 1
        if bit == 0:
            if prev_len == 0:
                prev_len = curr_len
                curr_len = 0
                if num & 2 == 0:
                    max_len = max(max_len, curr_len + prev_len + 1)
                    prev_len = 0
                    curr_len = 0

            else:
                max_len = max(max_len, curr_len + prev_len + 1)
                prev_len = 0
                curr_len = 0
        num = num >> 1
    add = 1 if prev_len > 0 else 0
    max_len = max(max_len, curr_len + prev_len + add)
    return max_len


num = 1775

print("Longest seq of 1 in %d by flipping one 0 to 1: %d" % (num, flip_win(num)))
