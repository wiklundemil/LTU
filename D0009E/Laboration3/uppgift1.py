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


#               ALTERNATIV 3              
def dictionaryfunc():
    dictionary_list={} 
    while 1 > 0:
        print("***** Dictionary *****")    
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        n = int(input())
        
        if n == 1:
            ord = input("Word to insert:")
            beskrivning = input("Discription of the word:")

            dictionary_list[ord]=beskrivning #Lägger till ett ny grupp baserad på ord och beskrivning inputen
        elif n == 2:
            print("Ordlistan:")
            for key, value in dictionary_list.items():
                print(key, sep="\n")
            n = input("Word to lookup:")
            print(dictionary_list[n]) #Printar ut den grupp med nyckeln n enligt
        else:
            print("Not valid...")
#               ALTERNATIV 2              
def tuplefunc():
    list_tupler = []
    while 1 > 0:
        print("***** Listor av tupler *****")
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        n = int(input())
        if n == 1:
            for item in list_tupler:
                print("Dessa är orden i listan:",item[0]) #För varje tupel i listna printar vi ut ordet (det med index 0)

            ord = input("Word to insert:")
            beskrivning = input("Discription of the word:")

            new_tuple = (ord, beskrivning)
            list_tupler.append(new_tuple)
        elif n == 2:
            print("Alla ord:",[i[0] for i in list_tupler]) #Tar alla ord med index 0 i enskilld tupel
            n = input("Word to lookup:")
            for item in list_tupler:
                if n in item:
                    print("Discription of the word:",item[1])    #Ger dig utskrift för det andra värdet i tuplern med ordet n i sig.
        elif n == 3:
            exit()
        else:
            print("Not valid...")

            
#               ALTERNATIV 1              
def listfunc():
    def list(x):
        ord = x
        return ord

    def list2(y):
        beskrivning = y
        return beskrivning


    ord = []
    beskrivning = []
    while 1 > 0:      
        print("***** Listor av strängar *****")
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        
        choice = int(input())
        if choice == 1:
            str_ord = input("Word to insert:")
            str_beskrivning = input("Discription of the word")

            result = list(str_ord)
            result2 = list2(str_beskrivning)
            lista = ord.append(result)
            lista2 = beskrivning.append(result2)
        elif choice == 2:
            print("Dessa är alla ord i ordlistan:",ord)
            n = input("Word to lookup:")
            if n in ord:
                index = ord.index(n)
                length = (len(ord))-1
                if index <= length:
                    print("Discription of the word:",beskrivning[index])
            else:
                print("Not valid...")
        elif choice == 3:
            print("Avslutar...")
            exit()


def menu():
    print("Skriv [1] för Listor av strängar.","Skriv [2] för listor av tupler.","Skriv [3] för dictionary.","Skriv [4] för att avsluta",sep="\n")
    choice = int(input("Vad vill du göra?"))

    if choice == 1:
        listfunc()
    elif choice == 2:
        tuplefunc()
    elif choice == 3:
        dictionaryfunc()
    elif choice == 4:
        print("Avslutar...")
        exit()
    
    else:
        print("Inte valbart")
    menu()
menu()