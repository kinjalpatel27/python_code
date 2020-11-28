def urlfy(ip_string, length):
    i = 0
    alpha = 0
    while i < len(ip_string):
        if ip_string[i] == " ":
            alpha += 1
            for j in range(length + alpha*2-1, i+2, -1):
                ip_string[j] = ip_string[j-2]
            ip_string[i] = "%"
            ip_string[i+1] = "2"
            ip_string[i+2] = "0"
            i += 3
            
        else:
            i += 1
    

    return ip_string

ip_string = "Mr John Smith    "
length = 13

def split(word): 
    return [char for char in word] 
print(urlfy(split(ip_string), length))