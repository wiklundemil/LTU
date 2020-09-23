def derivate(function,x,h):
    function_value = ((1/(2*h))*(function1(x + h) - function1(x - h))) #Sjävla formeln för derivatan
    return function_value  #ger funktionen det deriverade värdet

def function1(x):    #testfunktion 1
    value = x**2
    return value

# def function2(x):  #testfunktion 2
#     value = x**3
#     return value


# def function3(x):  #testfunktion 3
#     value = x**4
#     return value

