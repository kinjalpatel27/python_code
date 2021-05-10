def find_subset(set_val):
    if len(set_val) < 1:
        return [[]]

    elem = set_val.pop()
    inter_subset = find_subset(set_val)
    update_subset = []
    for sub in inter_subset:
        update_subset.append(sub + [elem])

    return inter_subset + update_subset


N = 4
set_val = list(range(N))
powerset = find_subset(set_val)
print("Power set ", powerset)
assert len(powerset) == 2 ** N
