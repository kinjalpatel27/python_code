def str_comp(string):
    rept = 1
    max_rept = 0
    comp_string = [string[0]]
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            rept += 1
        else:
            comp_string += str(rept)
            comp_string += string[i]
            max_rept = max(rept, max_rept)            
            rept = 1
    comp_string += str(rept)
    if max_rept == 1:
        return string
    else:
        return "".join(comp_string)

str1 = "abbbcddaddaaab"
print("\"%s\" compressed to \"%s\""%(str1, str_comp(str1)))