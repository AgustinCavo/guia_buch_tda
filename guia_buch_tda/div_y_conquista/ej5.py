def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    sorted_arr=[]
    izq=der=0
    while izq<len(left) and der<len(right):
        if left[izq]<=right[der]:
            sorted_arr.append(left[izq])
            izq+=1
        else:
            sorted_arr.append(right[der])
            der+=1
    sorted_arr.extend(left[izq:])
    sorted_arr.extend(right[der:])
    return sorted_arr
