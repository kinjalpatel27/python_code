def find_high(num):
    val = num
    idx = 0
    c1 = 0
    p = 0
    found = 0
    low_idx = -1
    high_idx = -1
    while val > 0:
        if val & (1 << 0):
            c1 += 1

            if (found & 1) == 0:
                p |= 1 << idx
                if ((val & 3) or 1) == 1:
                    high_idx = idx
                    found |= 1 << 0
            else:
                p |= 0 << idx

        if (val & 3) == 2 and ((found & 2) == 0):
            low_idx = idx + 1
            found |= 2
        if found & 3 == 3:
            break

        idx += 1
        val = val >> 1

    no_of_1 = 0
    for idx in range(c1 - 1):
        no_of_1 |= 1 << idx

    if high_idx > 0:
        high_num = (((num & ~p) & ~(1 << high_idx)) | (1 << high_idx + 1)) | no_of_1
    else:
        high_num = None

    if low_idx > 0:
        low_num = (num & ~(1 << low_idx)) | (1 << low_idx - 1)
    else:
        low_num = None

    return high_num, low_num


test_num = 5806
high_num, low_num = find_high(test_num)

print("Test number: ", bin(test_num), " , ", test_num)
if low_num is not None:
    print("Lower number with same 1's", bin(low_num), " , ", low_num)
else:
    print("Lower number with same 1's does not exist")
if high_num is not None:
    print("Higher number with same 1's", bin(high_num), " , ", high_num)
else:
    print("Higher number with same 1's does not exist")
