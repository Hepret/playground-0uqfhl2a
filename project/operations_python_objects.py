import math

from yml_pareser import ConfigObj


def square(in_put):
    if isinstance(in_put, (int,float,long)):
        value = in_put * in_put

    elif isinstance(in_put, list):
        value = []
        for i in in_put:
            value.append(i * i)
    elif isinstance(in_put, dict):
        value = {}
        for key in in_put.keys():
            value[key] = in_put[key] * in_put[key]
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


def cube(in_put):
    if isinstance(in_put, (int,float,long)):
        value = in_put * in_put * in_put

    elif isinstance(in_put, list):
        value = []
        for i in in_put:
            value.append(i * i * i)
    elif isinstance(in_put, dict):
        value = {}
        for key in in_put.keys():
            value[key] = in_put[key] * in_put[key] * in_put[key]
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


def factorial(in_put):
    if isinstance(in_put, (int,float,long)):
        value = math.factorial(in_put)

    elif isinstance(in_put, list):
        value = []
        for i in in_put:
            value.append(math.factorial(i))

    elif isinstance(in_put, dict):
        value = {}
        for key in in_put.keys():
            value[key] = math.factorial(in_put[key])
    else:
        raise Exception("Data Type to operate has not been implemented")
    return value


class Transform:
    def __init__(self):
        pass

    def execute(self, method, params):
        return eval(method)(params)
