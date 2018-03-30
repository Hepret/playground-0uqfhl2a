## Lets create some generic math operations on different python data types : this content is saved as operations_python_objects.py under project Directory

import math

def square(in_put):
    if isinstance(in_put,(int,float,long)):
        value = in_put * in_put

    elif isinstance(in_put,list):
        value = [i * i for i in in_put]

    elif isinstance(in_put,dict):
        value = {k: in_put[k] * in_put[k] for k in in_put.keys()}
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


def cube(in_put):
    if isinstance(in_put,(int,float,long)):
        value = in_put * in_put * in_put
    elif isinstance(in_put,list):
        value = [i * i * i for i in in_put]
    elif isinstance(in_put,dict):
        value = {k: in_put[k] * in_put[k] * in_put[k] for k in in_put.keys()}
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


def factorial(in_put):
    if isinstance(in_put,(int,float,long)):
        value = math.factorial(in_put)

    elif isinstance(in_put,list):
        value = [math.factorial(i) for i in in_put]

    elif isinstance(in_put,dict):
        value = {key: math.factorial(in_put[key]) for key in in_put.keys()}
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


class Transform:
    def __init__(self):
        pass

    def execute(self,method,params):
        return eval(method)(params)


## Using Pytests for testing above operations : this content is saved as test_operations_python_objects.py under project Directory

import pytest
from operations_python_objects import Transform


@pytest.fixture(scope='function')
def initi():
    obj = Transform()
    return obj

@pytest.mark.parametrize("in_put,out_put",[
    ('factorial;5',120),
    ('factorial;[1,2,3]',[1,2,6]),
    ("factorial;{'a':1,'b':2,'c':3}",{'a': 1,'b': 2,'c': 6}),

    ('cube;5',125),('cube;[1,2,3]',[1,8,27]),
    ("cube;{'a':1,'b':2,'c':3}",{'a': 1,'b': 8,'c': 27}),

    ('square;5',25),
    ('square;[1,2,3]',[1,4,9]),
    ("square;{'a':1,'b':2,'c':3}",{'a': 1,'b': 4,'c': 9})
])
def test_operations(initi,in_put,out_put):
    in_put1 = in_put.split(';')[0]
    in_put2 = in_put.split(';')[1]
    op = initi.execute(in_put1,eval(in_put2))
    assert op==out_put
    

## Finally, the running Py tests is very as you just have to goto terminal and run 'pytest -v' 
## Sample run looks as below:
(venv) indu-retina:project indu.sharma$ py.test -v         
============================================================= test session starts =============================================================
platform darwin -- Python 2.7.10, pytest-3.5.0, py-1.5.3, pluggy-0.6.0 -- /Users/indu.sharma/PycharmProjects/Practice/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/indu.sharma/Desktop/playground-cd9ep28h/project, inifile:
plugins: incremental-0.4.2
collected 9 items                                                                                                                             

test_operations_python_objects.py::test_operations[factorial;5-120] PASSED                                                              [ 11%]
test_operations_python_objects.py::test_operations[factorial;[1,2,3]-out_put1] PASSED                                                   [ 22%]
test_operations_python_objects.py::test_operations[factorial;{'a':1,'b':2,'c':3}-out_put2] PASSED                                       [ 33%]
test_operations_python_objects.py::test_operations[cube;5-125] PASSED                                                                   [ 44%]
test_operations_python_objects.py::test_operations[cube;[1,2,3]-out_put4] PASSED                                                        [ 55%]
test_operations_python_objects.py::test_operations[cube;{'a':1,'b':2,'c':3}-out_put5] PASSED                                            [ 66%]
test_operations_python_objects.py::test_operations[square;5-25] PASSED                                                                  [ 77%]
test_operations_python_objects.py::test_operations[square;[1,2,3]-out_put7] PASSED                                                      [ 88%]
test_operations_python_objects.py::test_operations[square;{'a':1,'b':2,'c':3}-out_put8] PASSED                                          [100%]

========================================================== 9 passed in 0.03 seconds ===========================================================
