def finder_rec(vec, n):
    if n==1:
        return None
    
    if n == 2:
        if vec[0] > vec[1] :
            return 0
        else:
            return None
        
    izq = vec[0:n//2]
    der = vec[n//2:n]    

    resu_izq = finder_rec(izq, len(izq))
    resu_der = finder_rec(der, len(der))

    if resu_izq is not None:
        return resu_izq
    if resu_der is not None:
        return resu_der + n//2
    
    if izq[-1] < der[0]:
        return None
    else:
        return n//2 - 1