import pytest 

@pytest.fixture(scope='function')
def initi():
    obj = Transform()
    return obj

@pytest.mark.parametrize("in_put,out_put",[('square;5',25),('factorial;[1,2,3]',[1,2,6])])
def test_operations(initi,in_put,out_put):
    in_put1=in_put.split(';')[0]
    in_put2 = in_put.split(';')[1]
    op = initi.execute(in_put1,eval(in_put2))
    assert op==out_put
