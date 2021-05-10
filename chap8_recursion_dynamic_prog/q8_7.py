def perm(orig_string):
    if len(orig_string) == 1:
        return [orig_string]

    strings = perm(orig_string[:-1])

    string_perm = []
    val = orig_string[-1]
    for string in strings:
        for i in range(1 + len(string)):
            comb = string[:i] + val + string[i:]
            string_perm.append(comb)
    return string_perm


print(perm("abc"))
