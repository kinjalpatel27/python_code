

s1 = "afdb"
s2 = "dbe"

def check_perm(s1, s2):
    s2_hash = {}
    if len(s2) < len(s1):
        return False
    for ind in range(len(s2)):
        if s2[ind] in s2_hash:
            s2_hash[s2[ind]] += 1
        else:
            s2_hash[s2[ind]] = 1

    perm = True
    for ind in range(len(s1)):
        if s1[ind] not in s2_hash:
            perm = False
            break

    return perm

print(check_perm(s1,s2))