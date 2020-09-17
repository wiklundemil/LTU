def derivate(function,x,h):
    function_value = ((1/(2*h))*(function3(x + h) - function3(x - h)))
    return function_value

# def function1(x):
#     value = x**2
#     return value

# def function2(x):
#     value = x**3
#     return value


def function3(x):
    value = x**4
    return value

print(derivate(function3,5,0.001))