def sparseSearch(array, string):
    left = 0
    right = len(array) - 1
    trial = 0
    while left <= right:
        idx = (left + right) // 2
        if array[idx] == string:
            break
        if array[idx] == "":
            idx_left = idx - 1
            idx_right = idx + 1

            while True:
                if idx_left < 0 or idx_right > len(array) - 1:
                    return -1
                else:
                    left_val = array[idx_left]
                    right_val = array[idx_right]
                if left_val != "":
                    if left_val == string:
                        return idx_left
                    if left_val > string:
                        right = idx_left + 1
                    else:
                        left = idx_left - 1
                elif right_val != "":
                    if right_val == string:
                        return idx_right
                    if right_val > string:
                        right = idx_right + 1
                    else:
                        left = idx_right - 1
                idx_left -= 1
                idx_right += 1

        else:
            if array[idx] > string:
                right = idx - 1
            else:
                left = idx + 1

    return idx


array = ["at", "", "", "", "", "ball", "", "", "", "", "car", "", "", "", "dad", "", ""]

idx = sparseSearch(array, "dad")
print(idx, " : ", array[idx])
