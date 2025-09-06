from ..ej3 import sqrt_int_rec   # import relativo desde la carpeta padre

def test_todo_entero():
    num=144
    assert sqrt_int_rec(num) == 12

def test_semi_entero_por_debajo():
    num=20
    assert sqrt_int_rec(num) == 4

def test_el_ultimo():
    num=93
    assert sqrt_int_rec(num) == 9

def test_grande():
    num=1478
    assert sqrt_int_rec(num) == 38

def test_chico():
    num=0.25
    assert sqrt_int_rec(num) == 0