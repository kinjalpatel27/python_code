def flip_num_bits(num1, num2):
    num = num1 ^ num2
    count = 0
    while num > 0:
        count += num & 1
        num = num >> 1
    return count


num1 = 58
num2 = 75
num_flip = flip_num_bits(num1, num2)
print("Number of bits to flip number %d to %d is %d" % (num1, num2, num_flip))
