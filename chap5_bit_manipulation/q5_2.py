def get_binary(num):
    if num >= 1 or num <= 0:
        raise Exception("Invalid number")
    binary = ["."]
    while num > 0:
        if len(binary) >= 32:
            raise Exception("Invalid number")
        num_up = num * 2
        num = num_up - int(num_up)
        if int(num_up) > 0:
            binary.append("1")
        else:
            binary.append("0")
    return binary


num = 2 ** (-10)
binary = get_binary(num)
print("Binary number for %f is %s" % (num, "".join(binary)))
