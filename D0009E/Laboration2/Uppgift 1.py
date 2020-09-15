def bounce(n, nreturn):
    if n == 0:
        rebounce(n, nreturn)
    else:
        print(n)
        bounce(n-1, nreturn) 

def rebounce(n, nreturn):
    if n == nreturn:
        print(n)
        print("Bounce complete")    
    else: 
        print(n)
        rebounce(n+1, nreturn)


def bounce2(n, nreturn):
    while n > 0:
        print(n)
        n = (n-1)
    if n == 0:
        rebounce2(n, nreturn)


def rebounce2(n, nreturn):
    while n < nreturn:
        print(n)
        n = (n+1)
    if n == nreturn:
        print(n)
        print("Bounce complete")

def tvarsumman(tal):
    if tal != 0:
        print("Bryter ut:",tal % 10)                 #Bryter ut och visar vilket resten av talet är.
        n1 = (tal - tal % 10) // 10                  #Skapar ett nytt tal genom att ta ("tal" - ("tal" % 10)) och köra heltalsdivision på parantesen.
        tvarsumman(n1)
    else:
        print("Inga fler siffror att bryta ut.")
 

def tvarsumman2(tal):
    lista_enskilda_tal = []
    while tal > 0:
        lista_enskilda_tal.append(tal % 10)         #Lägger till resten från "tal" % 10 och lägger till den i listan.
        tal = (tal - tal % 10) // 10                #Formeln för att få talet från exempelvis 100 till 10. Tar bort sista siffran ut tal.
    print("Här är alla enskilda siffror i det tidigare givna talet",lista_enskilda_tal)

n = int(input("Skriv en siffra:"))
nreturn = n                                          #nreturn sätts samma som n men nreturn förblir oförändrat i syfte att ha kvar det orginella talet av n.
#Kör när tvarsumman() funktionerna är bortkommenterade.
#bounce(n,nreturn)
#bounce2(n, nreturn)                                 #Skickar med n och nreturn som är ett fast tal i syfte att ha något  att jämföra med och gå tillaka till. 


#Kör när bounce funktionerna är bortkommenterade. Funktionerna innehåller samma input värde. Skriver man ett långt tal och anroppar bounce tar det väldigt lång tid.
tvarsumman2(n)
#tvarsumman(n)