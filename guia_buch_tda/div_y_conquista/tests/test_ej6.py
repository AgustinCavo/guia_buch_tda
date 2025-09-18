from ..ej6 import big_mult

def test_grandes():
    n1=1234
    n2=5678
    assert big_mult(n1,n2) ==7006652
        
def test_chicos():
    n1=1
    n2=7
    assert big_mult(n1,n2) ==7
def test_negativos():
    n1=1234
    n2=-5678
    assert big_mult(n1,n2) ==-7006652
    
def test_ceros():
    n1=0
    n2=5678
    assert big_mult(n1,n2) ==0
