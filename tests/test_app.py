from app import add

def test_add():
    assert add(2,6)==8
    assert add(-1,1)==0
    assert add(0,0)==0  # Test zero addition

def test_add_negative():
    assert add(-5, -3)==-8  # Test negative numbers

def test_add_positive():
    assert add(10, 5)==15  # Test positive numbers
  