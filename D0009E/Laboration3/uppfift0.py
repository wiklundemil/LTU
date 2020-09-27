def bounce(n):     
    if n==0:
        print(n)    #Påvägen tillbaka kommer den att printa ut alla "sparade" värden av n i det här fallet, 1,2,3 i just den ordningen.
    else: 
        print(n)
        bounce(n-1) 
        print(n)          


def bounce2(n):
    nreturn = n
    while n > 0:
        print(n)
        n = (n-1)
    while n-1 < nreturn:
        print(n)
        n = n+1


def tvarsumman(tal):
    if tal != 0:
        n1 = ((tal % 10) + tvarsumman(tal // 10))  
        return n1 #returnerar vi n1 kommer det se ut på följande när vi är i mitten 
                  #av rekursionen: return(3+2+1) + return 0.
                  #Detta kommer alltså att bli: return 6 + 0
    else:
        return 0


def tvarsumman2(tal):
    lista_enskilda_tal = []
    while tal > 0:
        lista_enskilda_tal.append(tal % 10)         #Lägger till resten från "tal" % 10 och lägger till den i listan.
        tal = (tal - tal % 10) // 10                #Formeln för att få talet från exempelvis 100 till 10. Tar bort sista siffran ut tal.
    return(sum(lista_enskilda_tal)) 



print("1. Kör bounce()", "2. Kör bounce2()", "3. Kör tvarsumman()", "4. Kör tvarsumman2()", sep="\n")
n = input("Vad vill du göra?")

if n=="1":
    print("*****bounce()*****")
    bounce(3)
elif n=="2":
    print("*****bounce2()*****")
    bounce2(3)
elif n=="3":
    print("*****tvarsumman()*****")
    print("Siffersumman är",tvarsumman(123),"av det givna värdet.")
elif n=="4":
    print("*****tvarsumman2()*****")
    print("Siffersumman är",tvarsumman(123),"av det givna värdet.")
else:
    print("Inte valbart.")
