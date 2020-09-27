ListaOrd = ["banan","kiwi","vindruva"]
BeskrivningOrd = ["Gul och ful","Grön och skön","Röd och äcklig"] 

n = input("skriv vilket av orden du vill ha beskrivning på:")

index = ListaOrd.index(n)
length = (len(ListaOrd))-1
print("length:",length)
if index <= length:
    print(BeskrivningOrd[index])
else:
    print("Inte tillgänlig.")