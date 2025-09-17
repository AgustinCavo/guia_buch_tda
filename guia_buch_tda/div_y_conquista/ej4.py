def max_pos_finder(arr, pos, length, arr_total=None):
    if arr_total is None:
        arr_total = arr  

    if len(arr) == 1:
        return pos

    mid = len(arr) // 2
    izq = max_pos_finder(arr[:mid], pos,        length, arr_total)
    der = max_pos_finder(arr[mid:], pos + mid,  length, arr_total)

    return izq if arr_total[izq] >= arr_total[der] else der