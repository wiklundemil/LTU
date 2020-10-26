#Skriv en rekursiv funktion sumTo(n) som summerar alla tal från och med 0 till och med n och returnerar dessa (obs! inte skriver uit på skärmen).
#Modifiera ovanstående funktion och döp den till sumFromTo. Funktionen tar två parametrar, start och stopp och returnerar summan av alla tal från och med start till och med stop.
#Skriv två små funktioner sumToUI() och sumFromToUI() som är användargränssnitt för respektive funktion (UI="User Interface"). sumToUI ska fråga användaren efter vilket tal som 
#ska summeras till, använda sumTo för att utföra uppgiften, och sedan skriva ut svaret på skärmen. sumFromToUI ska, på motsvarande sätt, fråga efter två tal för sumFromToUI.


def sumFromTo(start, stop):
    if stop == start:
        return 0
    else:
        return stop + sumFromTo(start, (stop-1))


def sumFromToUi():
    x = 0


def sumToUi():
    x = 0


start = int(input("Från:"))
stop = int(input("Till och med:"))

print("Summan av all tal i från",start,"och till och med", stop,"är:",sumFromTo(start, stop))
