from ..ej4 import max_pos_finder   # import relativo desde la carpeta padre

def test_mid():
    arr=[3,5,7,8,5,1]
    assert max_pos_finder(arr,0,len(arr)-1) == 3
    
def test_inicio():
    arr=[7,5,4,3,2,1]
    assert max_pos_finder(arr,0,len(arr)-1) == 0

def test_final():
    arr=[1,2,3,4,5,8,1]
    assert max_pos_finder(arr,0,len(arr)-1) == 5

def test_negativos():
    arr=[-2,-1,3,-1,-2]
    assert max_pos_finder(arr,0,len(arr)-1) == 2

