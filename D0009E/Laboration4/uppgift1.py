#-------------------Telefonboken------------------------#
class telefonbok:
    person = None
class person:
    name = None
    number = None

kalle = person()

#-------------------Telefonboken slut------------------------#
#-------------------Funktioner------------------------#
def addfunc():
    while True:
        print("ADD FUNKTION")
        print("[1], [2], [3]", sep="\n")
        n = int(input("Make a choice"))
        if n == 1:
            print("d")
        elif n == 2: 
            print("d")
        elif n == 3:
            print("Returning...")
            menu()

def lookupfunc():
    while True:
        print("LOOKUP FUNKTION")
        print("[1], [2], [3]", sep="\n")
        n = int(input("Make a choice"))
        if n == 3:
            print("Returning...")
            menu()

def aliasfunc():
    while True:
        print("ALIAS FUNKTION")
        print("[1], [2], [3]", sep="\n")
        n = int(input("Make a choice"))
        if n == 3:
            print("Returning...")
            menu()

def changefunc():
    while True:
        print("CHANGE FUNKTION")
        print("[1], [2], [3]", sep="\n")
        n = int(input("Make a choice"))
        if n == 1:
            olle = person()
            olle.number="9873"
        if n == 3:
            print("Returning...")
            menu()

def savefunc():
    while True:
        print("SAVE FUNKTION")
        print("[1], [2], [3]", sep="\n")
        n = int(input("Make a choice"))
        if n == 3:
            print("Returning...")
            menu()

def loadfunc():
    while True:
        print("LOAD FUNKTION")
        print("[1], [2], [3]", sep="\n")
        n = int(input("Make a choice"))
        if n == 3:
            print("Returning...")
            menu()

#-------------------Funktioner slut------------------------#
def menu():   
    print("[1] Add","[2] Lookup","[3] Alias","[4] Change","[5] Save","[6] Load","[0] Quit", sep="\n")
    n = int(input("Make a choice:")) #Denna behövde vara int för annars skickar den ett ssträng värde till if satserna. Det ska vara int.

    if n == 1:
        print("--- Add ---")
        addfunc()
    elif n == 2:
        print("--- Lookup ---")
        lookupfunc()
    elif n == 3:
        print("--- Alias ---")
        aliasfunc()
    elif n == 4:
        print("--- Change ---")
        changefunc()
    elif n == 5:
        print("--- Save ---")
        savefunc()
    elif n == 6:
        print("--- Load ---")
        loadfunc()
    elif n == 0:
        print("--- Quit ---")    
        exit()
    else:
        print("Not valid...")    
menu()