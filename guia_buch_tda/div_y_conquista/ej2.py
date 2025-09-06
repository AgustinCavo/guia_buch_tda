def finder_zero_rec(vec,n):
    if len(vec)==1:
        if vec[0]==0:
            return 0+n-1
        else:
            return -1
                   
    izq=vec[0:n//2]
    der=vec[n//2:n]
    resu_izq=finder_zero_rec(izq,n//2)
    resu_der=finder_zero_rec(der,n-n//2)
 
    if resu_izq != -1:
        return resu_izq
    if resu_der != -1:
        return resu_der + n//2
    
    return -1