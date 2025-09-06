from ..ej2 import finder_zero_rec   # import relativo desde la carpeta padre

def test_en_la_mitad():
    vec=[1,1,0,0,0]
    assert finder_zero_rec(vec,len(vec)) == 2

def test_el_segundo():
    vec=[1,0,0,0,0]
    assert finder_zero_rec(vec,len(vec)) == 1

def test_el_ultimo():
    vec=[1,1,1,1,0]
    assert finder_zero_rec(vec,len(vec)) == 4

def test_todo_mal():
    vec=[0,0,0,0,0]
    assert finder_zero_rec(vec,len(vec)) == 0

def test_todos_bien():
    vec=[1,1,1,1,1]
    assert finder_zero_rec(vec,len(vec)) == -1