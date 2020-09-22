def derivate(f,x0,h):       #Deriverings funktionen
    value = ((1/(2*h))*(f(x0 + h) - f(x0 - h)))  #använder f-funktionen i formeln
    return value    #Ger funktionen värdet value


def f(x):               #Skapar funktionen f.
    f = x**2            
    return f            #funktionen får värdet f


def solve(f,x0,h):  #Använder sig av funktionen f samt funktionen derivate 
    x1 = x0 + (2*h)     
    while abs(x0 - x1) > h:  #Medans skillnaden är större än h så kör vi loopen
        x1 = x0
        x0 = x0 - (f(x0)/derivate(f,x0,h))

    return x0   #Om skillnaden inte är större än h ger vi funktionen värdet av x0


print("Värdet av funktionen solve blir",solve(f,1475069,3))