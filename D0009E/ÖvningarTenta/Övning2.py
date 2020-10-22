#Modifiera lösningen på uppgiften från föreläsning 2 så att den frågar användaren efter vilken tabell som ska skrivas ut.
#Skriv också om själva utskriften, så att denna finns i en egen funktion, som bara skriver ut en enda rad, och som anropas
#där det behövs. Funktionen ska ta två parametrar: vilken tabell som ska skrivas ut, samt vilken rad i tabellen som ska skrivas ut.
def multiplication(tabell, rad):
    print(tabell, "*", rad, "=", tabell*rad)

multiplication(2, 4)