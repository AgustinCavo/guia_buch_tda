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
    

vec=[1,2,3,4,5,11,7,8,9,10]
vec2=[12,20,30,40,50,70,80,90,11]
vec3=[1,2,3,4,5,7,8,9,]
vec4=[11,2,3,4,5,6,7,8,9,10]

print(finder_rec(vec,len(vec)))
print(finder_rec(vec2,len(vec2)))
print(finder_rec(vec3,len(vec3)))
print(finder_rec(vec4,len(vec4)))