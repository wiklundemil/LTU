def derivate(f,x0,h):       #Deriverings funktionen
    value = ((1/(2*h))*(f(x0 + h) - f(x0 - h)))  #använder f-funktionen i formeln
    return value    #Ger funktionen värdet value


def solve(f,x0,h):  #Funktionens syfte är att 
    x1 = x0 + h     #
    while abs(x0 - x1) > h:
        x1 = x0
        x0 = x0 - (f(x0)/derivate(f,x0,h))

    return x0

def f(x):               #Skapar funktionen f.
    f = x**2            
    return f            #funktionen får värdet f


print(solve(f,0,0.0001))