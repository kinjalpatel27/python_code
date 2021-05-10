def pair_shit(num):
    return ((num & 0x5555555555555555) << 1) | ((num & 0xAAAAAAAAAAAAAAAA) >> 1)


test_num = 58
print("pairwise shifted # for ", bin(test_num), " is ", bin(pair_shit(test_num)))
