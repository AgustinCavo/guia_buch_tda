def big_mult(n1,n2):
    if n1<10 or n2<10:
        return n1*n2
    else:
        n1_str=str(n1)
        n2_str=str(n2)
        cantidad_digitos_parte_baja=max(len(n1_str),len(n2_str))
        if cantidad_digitos_parte_baja%2!=0:
            cantidad_digitos_parte_baja+=1
        cantidad_digitos_parte_baja=cantidad_digitos_parte_baja//2
        parte_alta_n1=int(n1_str[:-cantidad_digitos_parte_baja]) if n1_str[:-cantidad_digitos_parte_baja] else 0
        parte_baja_n1=int(n1_str[-cantidad_digitos_parte_baja:])
        parte_alta_n2=int(n2_str[:-cantidad_digitos_parte_baja]) if n2_str[:-cantidad_digitos_parte_baja] else 0
        parte_baja_n2=int(n2_str[-cantidad_digitos_parte_baja:])

        e1=big_mult(parte_alta_n1,parte_alta_n2)
        e2=big_mult(parte_baja_n1,parte_baja_n2)
        e3=big_mult(parte_alta_n1+parte_baja_n1,parte_alta_n2+parte_baja_n2)-e1-e2

        return e1*(10**(2*cantidad_digitos_parte_baja))+e3*(10**cantidad_digitos_parte_baja)+e2
    
    

