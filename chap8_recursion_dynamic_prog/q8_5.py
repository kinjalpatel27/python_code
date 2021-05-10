num1 = 11
num2 = 13


def get_sort(num1, num2):
    small_num = min(num1, num2)
    big_num = max(num1, num2)
    return small_num, big_num


def recursive_mul(smaller, bigger, sort=True):
    if sort:
        smaller, bigger = get_sort(num1, num2)
        sort = False
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller >> 1
    half_prod = recursive_mul(s, bigger, sort)

    if smaller & 1 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger


multiply = recursive_mul(num1, num2)
print(num1, " * ", num2, " = ", multiply)
