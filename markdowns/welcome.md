## Lets create some generic math operations on different python data types. 
```
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
```

## Lets write the pytests code for testing above functions.
```
@[Luke, How can you parametrize all the tests in one go?]({"stubs": ["universe.py"], "command": "python3 test_operations_python_objects.py"})

```

## Finally, running the Py tests is very easy as you just have to goto terminal and run 'pytest -v' 

*Test Cases*                                                        | *Status*               | *percentage*


--------------------------------------------------------------------| ------------------------|-----------------
test_operations_python_objects.py::test_operations[factorial;5-120] |PASSED | [ 11%]
test_operations_python_objects.py::test_operations[factorial;[1,2,3]-out_put1] |PASSED |[ 22%]
test_operations_python_objects.py::test_operations[factorial;{'a':1,'b':2,'c':3}-out_put2] |PASSED  |[ 33%]
test_operations_python_objects.py::test_operations[cube;5-125]| PASSED    |     [ 44%]
test_operations_python_objects.py::test_operations[cube;[1,2,3]-out_put4]| PASSED   |  [ 55%]
test_operations_python_objects.py::test_operations[cube;{'a':1,'b':2,'c':3}-out_put5]| PASSED   |   [ 66%]
test_operations_python_objects.py::test_operations[square;5-25] |PASSED    |    [ 77%]
test_operations_python_objects.py::test_operations[square;[1,2,3]-out_put7] |PASSED  | [ 88%]
test_operations_python_objects.py::test_operations[square;{'a':1,'b':2,'c':3}-out_put8]| PASSED       | [100%]


#9 Test Cases passed in 0.03 seconds
