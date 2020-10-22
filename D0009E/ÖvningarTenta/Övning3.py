#Modifiera lösningen från föreläsning 3
#så att den inte innehåller upprepad kod utan använder rekursion och villkor istället. Extrauppgift: Låt programmet fråga även efter start och stopp-värde för tabellen.

def multiplication(tabell, rad, stopvalue):
    if tabell*rad < stopvalue:
        print(tabell, "*", rad, "=", tabell*rad)
        rad = rad+1
        multiplication(tabell, rad,stopvalue)
    else:
        print("Stopvärde nått...")


print("Tal1 * Tal2. Stopvärde menar på där programmet ska stanna innan.")
Tal1 = int(input("skriv Tal1"))
Tal2 = int(input("skriv Tal2"))
stopvalue = int(input("skriv stopvalue"))
multiplication(Tal1, Tal2, stopvalue)

