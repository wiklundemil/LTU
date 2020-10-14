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


#                ALTERNATIV 3 
def lookup_dict(x):
    dictionary_list = x

    print("Ordlistan:")
    for key, value in dictionary_list.items(): #För varje key och value, i dictionary_list.items() .items tyder på föremålen i listan dessa{'a':'b'} 
        print(key, sep="\n")    #Listar alla keys i varje "list" som finns i den större listan dictionary_list
    n = input("Word to lookup:")  #Ordet du vill kolla upp
    print(dictionary_list[n]) #Printar ut den grupp med nyckeln n enligt
    return dictionary_list 
 
def insert_dict(x):
    dictionary_list = x
    
    ord = input("Word to insert:")  #Ger användarn möjlighet att ange ett ord
    for num in dictionary_list: #num = keys, För varje nyckel gör detta:
        if ord == num: # För varje nyckel kolla om användar input är lika med nyckeln.
            print("Ord existerar redan")
            return dictionary_list
    else:
        beskrivning = input("Discription of the word:") #Ger användarn möjlighet att ange ett beskrivning

        dictionary_list[ord]=beskrivning #Lägger till ett ny grupp baserad på ord och beskrivning inputen
    return dictionary_list

def dictionaryfunc():
    dictionary_list={} #Skapar listan innan loopen så att den alltid existerar med samma värden som lagts till.
    while True:
        print("***** Dictionary *****")    
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        n = int(input())
        
        if n == 1:
            insert_dict(dictionary_list)
        elif n == 2:
            lookup_dict(dictionary_list)
        elif n == 3:
            print("Avslutar...")
            break
        else:
            print("Not valid...")



#                 ALTERNATIV 2 
def insert_tupl(x):
    list_tupler = x
    # for item in list_tupler: #För varje föremål i listan med tupler, föremål = tupeln 
    #     print("Dessa är orden i listan:",item[0]) #För varje tupel i listna printar vi ut ordet (det med index 0)

    ord = input("Word to insert:")  #Ger användarn möjlighet att ange ett ord
    for num in list_tupler:
        if ord == num[0]:
            print("Ord existerar redan")
            return list_tupler
    else:
        beskrivning = input("Discription of the word:") #Ger användarn möjlighet att ange en beskrivning

        new_tuple = (ord, beskrivning) #Här skapar man en tuple
        list_tupler.append(new_tuple) #Här lägger man till new_tuple variabeln i listan av tuples
    return list_tupler

def lookup_tupl(x):
    list_tupler = x

    print("Alla ord:",[i[0] for i in list_tupler]) #Tar alla ord med index 0 i enskilld tupel
    n = input("Word to lookup:")
    for item in list_tupler:    #För varje föremål i listan med tuples
        if n in item:   #Om ordet du vill kolla upp finns i föremålet, föremålet = tupeln
            print("Discription of the word:",item[1])    #Ger dig utskrift för det andra värdet i tuplern med ordet n i sig.
    return list_tupler

def tuplefunc():
    list_tupler = []   #Skapar listan innan loopen så att den alltid existerar med samma värden som lagts till.
    while True:
        print("***** Listor av tupler *****")
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        n = int(input())
        if n == 1:
            insert_tupl(list_tupler)
        elif n == 2:
            lookup_tupl(list_tupler)
        elif n == 3:
            print("Avslutar...")
            break
        else:
            print("Not valid...")
   
#               ALTERNATIV 1   
def lookup_list(x, y):
    ord = x
    beskrivning = y

    print("Dessa är alla ord i ordlistan:",ord) #listar alla ord som finns i listan ord
    n = input("Word to lookup:") #Ger användaren möjlighet att slå upp ett ord som de skrivit
    if n in ord: #Om ordet användaren skrivit in finns i listan med ord
        index = ord.index(n) #kollar det indexet på ordet som användaren valt
        length = (len(ord))-1 #Kollar längden på listan och tar det -1 för att man vill ha index
    if index <= length: #Om index är mindre eller lika med längden på listan
        print("Discription of the word:",beskrivning[index]) #Listar ut beskrivingen till ordet med samma index som beskrivningen 
    else:
        print("Not valid...")
    return (ord, beskrivning)

def insert_list(x, y):
    ord = x
    beskrivning = y
    
    str_ord = input("Word to insert:") #Ger användarn möjlighet att ange ett ord
    if str_ord in ord:
        print("Ord finns redan...")
        return(ord, beskrivning)

    str_beskrivning = input("Discription of the word")#Ger användarn möjlighet att ange en beskrivning

    ord.append(str_ord) #Lägger till det inmatade värdet i listan för ord
    beskrivning.append(str_beskrivning)  #Lägger till det inmatade värdet i listan för beskrivningar
  
    return (ord, beskrivning)

def listfunc():

    ord = []     #Skapar listan innan loopen så att den alltid existerar med samma värden som lagts till.
    beskrivning = []    #Skapar listan innan loopen så att den alltid existerar med samma värden som lagts till.
    while True:      
        print("***** Listor av strängar *****")
        print("[1] Insert","[2] Lokup","[3] Exit program",sep="\n")
        
        choice = int(input()) #vad vill användaren göra, användaren matar in en siffra för att välja alternativ
        if choice == 1:
           insert_list(ord, beskrivning)
        elif choice == 2:
            lookup_list(ord, beskrivning)
        elif choice == 3:
            print("Avslutar...")
            break

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