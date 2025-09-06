def sqrt_int_rec(num):
    if num < 0:
        return -1
    if num < 1:
        return 0
    if num == 1:
        return 1
    

    def aux_sqrt_int_rec(num, low, high):
        mid=(low + high) // 2

        if (mid*mid) == num:
            return mid
        if (mid*mid) < num and ((mid+1)*(mid+1)) > num:
            return mid
        if (mid*mid) < num:
            return aux_sqrt_int_rec(num, mid+1, high)
        else:
            return aux_sqrt_int_rec(num, low, mid-1)

    return aux_sqrt_int_rec(num, 1, num//2)

