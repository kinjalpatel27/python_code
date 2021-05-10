test_string = {}


def perm(string):
    global test_string
    test_string = convert_hash(string)
    return get_perm(list(test_string.keys()))


def convert_hash(string):
    hashmap = {}
    for char in string:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    return hashmap


def get_perm(chars):
    if len(chars) == 1:
        string_perm = []
        for _ in range(test_string[chars[0]]):
            string_perm.append(chars)
        return string_perm

    strings = get_perm(chars[:-1])

    curr_char = chars[-1]
    n_curr_char = test_string[curr_char]
    pairs = []
    for i in range(1, 1 + n_curr_char):
        first = []
        sec = []
        for _ in range(i):
            first.append(curr_char)
        for _ in range(n_curr_char - i):
            sec.append(curr_char)
        pairs.append([first, sec])

    string_perm = []
    for string in strings:
        for i in range(1 + len(string)):
            if len(pairs) > 1:
                for j in range(i + 1, 1 + len(string)):
                    for first, sec in pairs:
                        comb = string[:i] + first + string[:j] + sec + string[j:]
                        string_perm.append(comb)
                        if sec == []:
                            comb = string[:i] + string[:j] + first + string[j:]
                            string_perm.append(comb)

            else:
                comb = string[:i] + [curr_char] + string[i:]
                string_perm.append(comb)
    return string_perm


all_comb = perm(["a", "b", "c", "e", "e", "e", "b"])
test = {}
for comb in all_comb:
    key_val = "".join(comb)
    if key_val in test:
        test[key_val] += 1
        AssertionError("Duplicates")
    else:
        test[key_val] = 1
