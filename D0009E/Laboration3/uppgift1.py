# ListaOrd = ["banan","kiwi","vindruva"]
# BeskrivningOrd = ["Gul och ful","Grön och skön","Röd och äcklig"] 

# print("Dessa är alla ord i ordlistan:",ListaOrd)
# n = input("Skriv vilket av orden du vill ha beskrivning på:")

# index = ListaOrd.index(n)
# length = (len(ListaOrd))-1
# print("length:",length)
# if index <= length:
#     print(BeskrivningOrd[index])
# else:
#     print("Inte tillgänlig.")


def tuplefunc():
    list_tupler = [("banan", "Gul och ful") ,("kiwi", "Grön och skön"), ("vindruva", "Röd och äcklig")]
    for item in list_tupler:
        print("Dessa är orden i listan:",item[0]) #För varje tupel i listna printar vi ut ordet (det med index 0)

    ord = input("Skriv det ord du vill lägga till:")
    beskrivning = input("Skriv den beskrivning du vill lägga till:")

    new_tuple = (ord, beskrivning)
    list_tupler.append(new_tuple)

    print(list_tupler)
    n = input("Skriv vad för ord du vill söka upp:")
    for item in list_tupler:
        if n in item:
            print(item[1])    #Ger dig utskrift för det andra värdet i tuplern med ordet n i sig.


def dictionaryfunc():
    dictionary_list={'banan': 'gul och ful', 'kiwi': 'grön och skön', 'vindruva':'röd och äcklig'}

    ord = input("Skriv det [ord] du vill lägga till:")
    beskrivning = input("Skriv den beskrivning du vill lägga till:")

    dictionary_list[ord]=beskrivning #Lägger till ett ny grupp baserad på ord och beskrivning inputen

    print(dictionary_list)    #Printar listan för att kontrolera att gruppen lades till
    n = input("Skriv det ord som du vill slå upp:")
    print(dictionary_list[n]) #Printar ut den grupp med nyckeln n enligt


def listfunc():
    choice = int(input("Vad vill du göra?"))
    ord = []
    beskrivning = [] 
    if choice == 1:
        new_ord = input("Word to insert:")
        new_beskrivning = input("Discription of word:")

        ord.append(new_ord)
        beskrivning.append(new_beskrivning)
        print("Lade till:",ord, beskrivning)
        
        result = (ord, beskrivning)
        return result
    elif choice == 2:
        print("Dessa är alla ord i ordlistan:",ord)
        n = input("Skriv [ord] du vill ha beskrivning på:")
        if n in ord:
            index = ord.index(n)
            length = (len(ord))-1
            print("length:",length)
            if index <= length:
                print(beskrivning[index])
            else:
                print("Not valid...")
    else:
        print("Exiting...")


def menu():
    print("Skriv [1] för Listor av strängar.","Skriv [2] för listor av tupler.","Skriv [3] för dictionary.","Skriv [4] för att avsluta",sep="\n")
    choice = int(input("Vad vill du göra?"))

    if choice == 1:
        print("***** Listor av strängar *****")
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        listfunc()
    elif choice == 2:
        print("***** Listor av tupler *****")
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        tuplefunc()
    elif choice == 3:
        print("***** Dictionary *****")    
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        dictionaryfunc()
    elif choice == 4:
        print("Avslutar...")
        exit()
    
    else:
        print("Inte valbart")
    menu()
menu()