def perm_palnd(ip_string):
    hashmap = {}
    for i in range(len(ip_string)):
        char = ip_string[i].lower()
        if char in list(hashmap.keys()):
            hashmap[char] += 1
        else:
            hashmap[char] = 1
    
    odd = 0

    for key in hashmap.keys():
        if key == " ":
            continue
        if hashmap[key] % 2 != 0:
            if odd == 0:
                odd += 1
            else:
                return False

    return True

string = "Tact Coa"
ans = "" if perm_palnd(string) else "not"
print("\"%s\" is %s palindrom"%(string, ans))

string = "Tact Koa"
ans = "" if perm_palnd(string) else "not"
print("\"%s\" is %s palindrom"%(string, ans))