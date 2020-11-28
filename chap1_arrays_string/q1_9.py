def string_rot(str1, str2):
    if len(str1) != len(str2):
        return False

    str3 = str1+str1
    if str2 in str3:
        return True
    else:
        return False

str1 = "waterbottle"
str2 = "tlewaterot"
ans = "a" if string_rot(str1, str2) else "not"
print("\"%s\" is %s rotation of \"%s\""%(str1, ans, str2))

str1 = "waterbottle"
str2 = "tlewaterbot"
ans = "a" if string_rot(str1, str2) else "not"
print("\"%s\" is %s rotation of \"%s\""%(str1, ans, str2))
