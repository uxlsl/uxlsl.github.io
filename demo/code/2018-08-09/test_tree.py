from tree import Node


def test_isSame():
    n1 = Node(None, None, 1)
    n2 = Node(None, None, 1)
    n3 = Node(None, n2, 1) 
    n4 = Node(None, n2, 1) 
    n5 = Node(n1, n2, 3) 
    n6 = Node(n1, n2, 3) 
    n7 = Node(n1, n4, 3) 
    n8 = Node(n4, n2, 3) 
    assert n1.IsSame(n2) == True
    assert n1.IsSame(None) == False
    assert n1.IsSame(n3) == False
    assert n3.IsSame(n4) == True
    assert n5.IsSame(n6) == True
    assert n5.IsSame(n7) == False
    assert n5.IsSame(n8) == False
