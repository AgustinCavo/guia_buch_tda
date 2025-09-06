from ..ej1 import finder_rec   # import relativo desde la carpeta padre

def test_en_la_mitad():
    vec=[1,2,3,4,5,11,7,8,9,10]
    assert finder_rec(vec,len(vec)) == 5

def test_al_final():
    vec=[12,20,30,40,50,70,80,90,11]
    assert finder_rec(vec,len(vec)) == 7

def test_al_principio():
    vec=[120,20,30,40,50,70,80,90]
    assert finder_rec(vec,len(vec)) == 0