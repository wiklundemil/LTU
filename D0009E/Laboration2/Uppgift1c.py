def tvarsumman(tal):
    if tal != 0:
        print("Bryter ut:",tal % 10)                 #Bryter ut och visar vilket resten av talet är.
        n1 = (tal - tal % 10) // 10                  #Skapar ett nytt tal genom att ta ("tal" - ("tal" % 10)) och köra heltalsdivision på parantesen.
        tvarsumman(n1)
    else:
        print("Inga fler siffror att bryta ut.")
 

n = int(input("Skriv en siffra:"))
tvarsumman(n)