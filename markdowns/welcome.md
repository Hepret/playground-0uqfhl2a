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

https://tech.io/snippet/wYJufUl

## Finally, the running Py tests is very as you just have to goto terminal and run 'pytest -v' 
## Sample run looks as below:
'''
collected 2 items                                                                                                                             
test_functions.py::test_operations[square;5-25] PASSED                                                                                  [ 50%]
test_functions.py::test_operations[factorial;[1,2,3]-out_put1] PASSED                                                                   [100%]
================================================= 2 passed in 0.04 seconds
'''
