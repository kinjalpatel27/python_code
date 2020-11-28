def is_unique(ip_string):
    hashmap = {}
    unique = True
    for i in range(len(ip_string)):
        if ip_string[i] in hashmap:
            hashmap[ip_string[i]] += 1
        else:
            hashmap[ip_string[i]] = 1

    for key in hashmap.keys():
        if hashmap[key] > 1:
            unique = False
            break
    return unique

ip_string = "teaisokay"
unique = is_unique(ip_string)
ans = "not" if not unique else ""
print("\"%s\" is %s unique"%(ip_string,ans))

ip_string = "teaisok"
unique = is_unique(ip_string)
ans = "not" if not unique else ""
print("\"%s\" is %s unique"%(ip_string,ans))
