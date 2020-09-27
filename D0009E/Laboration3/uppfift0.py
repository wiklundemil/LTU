import math
def bounce(n):     
    if n==0:
        print(n)    #Påvägen tillbaka kommer den att printa ut alla "sparade" värden av n i det här fallet, 1,2,3 i just den ordningen.
    else: 
        print(n)
        bounce(n-1) 
        print(n)          


def tvarsumman(tal):
    if tal != 0:
        n1 = ((tal % 10) + tvarsumman(tal // 10))  
        return n1 #returnerar vi n1 kommer det se ut på följande när vi är i mitten 
                  #av rekursionen: return(3+2+1) + return 0.
                  #Detta kommer alltså att bli: return 6 + 0
    else:
        return 0


def derivate(f,x0,h):       #Deriverings funktionen
    value = ((1/(2*h))*(f(x0 + h) - f(x0 - h)))  #använder f-funktionen i formeln
    return value    #Ger funktionen värdet value


def solve(f,x0,h):  #Använder sig av funktionen f samt funktionen derivate 
    x1 = x0 + (2*h)     
    while abs(x0 - x1) > h:  #Medans skillnaden är större än h så kör vi loopen
        x1 = x0
        x0 = x0 - (f(x0)/derivate(f,x0,h))

    return x0   #Om skillnaden inte är större än h ger vi funktionen värdet av x0


def f(x):               #Skapar funktionen f.
    f = (x**2)-1           
    return f            #funktionen får värdet f


def menu():    
    print("1. Kör bounce()", "2. Kör tvarsumman()", "3. Kör Newton-Raphson()", "4. Avsluta", sep="\n")
    n = input("Vad vill du göra?")

    if n=="1":
        print("*****bounce()*****")
        bounce(3)
        menu()
    elif n=="2":
        print("*****tvarsumman()*****")
        print("Siffersumman är",tvarsumman(123),"av det givna värdet 123.")
        menu()
    elif n=="3":
        print("*****Newton-Raphson()*****")
        print("Löser med f(x)=x^2-1")
        solve(n,5,0.01)

        menu()
    elif n=="4":
        print("Avslutar...")
        
    else:
        print("Inte valbart.")
        menu()
menu()

#något med rad 54 