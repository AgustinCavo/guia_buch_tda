from ..ej5 import merge_sort   # import relativo desde la carpeta padre

def test_mid():
    arr=[3,5,7,8,5,1]
    assert merge_sort(arr) ==[1,3,5,5,7,8]
    
def test_inicio():
    arr=[7,5,4,3,2,1]
    assert merge_sort(arr) == [1,2,3,4,5,7]

def test_final():
    arr=[1,2,3,4,5,8,1]
    assert merge_sort(arr) == [1,1,2,3,4,5,8]

def test_negativos():
    arr=[1,2,3,2,1]
    assert merge_sort(arr) == [1,1,2,2,3]

