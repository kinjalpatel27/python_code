def one_away(str1, str2):
    diff = 0
    ind1 = 0
    ind2 = 0
    if abs(len(str1) -len(str2)) > 1:
        return False

    first = str1 if len(str1) > len(str2) else str2
    sec = str2 if len(str2) > len(str1) else str1

    while ind1 < len(first) and ind2 < len(sec):
        if first[ind1] != sec[ind2]:
            if diff == 0:
                diff += 1
            else:
                return False
            if len(first) == len(sec):
                ind2 += 1
        else:
            ind2 += 1

        ind1+=1

        
    return True


str1="pale"
str2s=["ple","ple","pales","bake","apale","ples"]

for str2 in str2s:
    ans = "" if one_away(str1,str2) else "not"
    print("\"%s\" and \"%s\" is %s one away"%(str1,str2,ans))
