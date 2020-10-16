#-------------------Telefonboken------------------------#
class telefonbok:
    def __init__(self):
        self.dictionary = {}            #dictionary
        self.dictionaryAlias = {}       #dictionary av aliasen
    # -------------- Metoder ---------------#
    def add(self, name, number):
        if name in self.dictionary or number in self.dictionary.values(): #Kontrollerar om nummer eller name finns som key eller value...
            print("Namn eller Nummer existerar redan") #Printar ut att namn eller nummer finns redan
        else: 
             self.dictionary[name] = number  #lägger till i dictionary en nyckel name och sitt value number. Värdena tas från parametern


    def lookup(self, name):
        if name in self.dictionary:   #Om namn finns som nyckel i dictionary
            print(self.dictionary[name])        #Skriv ut value av nyckeln name
        else:
            if name in self.dictionaryAlias:    #om name finns i dictionaryAlias 
                while name in self.dictionaryAlias: #Startar en loop där man kollar upp det orginella namnet.
                    name = self.dictionaryAlias[name]   #Eftersom dictionaryAlias pekar på föregående namn ex om Emil har value 0709840002. Sätter man ett alias på Emil blir följande alias Emil David i dictionaryAlias lika med {David : Emil}  alias pekar på föregående namn
                print(self.dictionary[name])    #Printar ut value från nyckeln name ur dictionary

    def alias(self, name, newname):
        if name not in self.dictionary:  #Om namn inte finns i dictionary
            if name in self.dictionaryAlias:    #Om namn finns i dictionaryAlias 
                self.dictionaryAlias[newname] = name #Sätt newname som nyckel till det namn du skrev in (name)
            else:
                print("name not found or duplicated name") #Om namn inte finns i dictionaryAlias ge ett felmedelande
        else:
            if name in self.dictionary and newname in self.dictionary:  #else om namn finns i dictionary och ocså om newname finns i dictionary som nycklar
                print("name not found or duplicated name")               #Print att det finns en dubblet
            else:
                self.dictionaryAlias[newname] = name        #Om namn inte finns i dictionary och om också newname inte finns dictionary som nycklar

    def change(self, name, number):
        if name in self.dictionary:
            self.dictionary[name] = number
       
        elif name in self.dictionaryAlias.keys() and number not in self.dictionary.values():
            while name in self.dictionaryAlias:
                name = self.dictionaryAlias[name]
            self.dictionary[name] = number
        else:
            print("not found or trying to overwrite")
        # if name not in self.dictionary and name not in self.dictionaryAlias: #Om namn inte är en nyckel i dictionary eler dictionaryAlias 
        #     print("not found")  #Inte finns alltså 
        # else:
        #     if name in self.dictionaryAlias or name in self.dictionary: #Else om namn finns som nyckel i dictionaryAlias eller namn är en nyckel i dictionary
        #         while name in self.dictionaryAlias: #Startar en loop där man kollar upp det orginella namnet.
        #             name = self.dictionaryAlias[name]   #Eftersom dictionaryAlias pekar på föregående namn ex om Emil har value 0709840002. Sätter man ett alias på Emil blir följande alias Emil David i dictionaryAlias lika med {David : Emil}  alias pekar på föregående namn
        #         self.dictionary[name] = number     #Använder det namn som fås ut av while loopen. Denna är nyckeln och även orginalnamnet till nummer 
        #     elif name in self.dictionaryAlias.values():
        #         print("Not found")
    def save(self, filnamn):
        fil = open(filnamn, "w")  #Öppnar en ny fil för skrivning
        for obj in self.dictionary: # för varje object i dictionary 
            values = self.dictionary[obj]   #sätter variabeln values till dictionaryts value av dictionaryts nycklar (obj). 
            fil.write(values + ";"+ obj+"\n") #Skriver i filen Nummer + ; + Namn
        
        for obj2 in self.dictionaryAlias:
            values_name = self.dictionaryAlias[obj2]
            if values_name in self.dictionary:
                nummervar = self.dictionary[values_name]
                fil.write(nummervar+";"+obj2+"\n")
        fil.close() #Stänger filern


    def load(self, filnamn):    
        fil = open(filnamn, "r")    #Öppnar filen för läsning
        lines = fil.readlines()     #Sätter variabeln lines som är enskildrad
        for line in lines:          #För varje line i filen
            val1 = line.split(";")  #Sätter val1 till raden utan ;
            number = val1[0]        #sätter number till det första valuet med index 0 i listan som split skapar [nummer, namn]
            name = val1[1][:-1]     #sätter namn till det andra valuet med index 1 i listan som split skapar [nummer, namn]
            self.dictionary[name] = number #Lägger till samtliga värden i telefonbokens dictionary = {}
        fil.close()                 #Stänger filen

    # -------------- Metoder slut ---------------#
    
    # ------------- Prompt -------------#
    def prompt():                           
        person = telefonbok()       #Skapar ett object person
        while True:                 
            n = input("telebok>").split()   #Användar inputen som kallas för n
            if n[0] == "add":           #Om den första inputen = index 0 är likadan som strängen gör detta...
                    name    = n[1]          #Sätter variabeln till input 2
                    number  = n[2]          #Sätter variabeln till input 3
                    person.add(name, number)#Går in i objectet person till methoden och skickar med varieblernas värden
                
            elif n[0] == "lookup":      #Om den första inputen = index 0 är likadan som strängen gör detta...
                    name    = n[1]          #Sätter variabeln till input 2
                    person.lookup(name)
                
            elif n[0] == "alias":       #Om den första inputen = index 0 är likadan som strängen gör detta...
                    name    = n[1]          #Sätter variabeln till input 2
                    newname = n[2]          #Sätter variabeln till input 3
                    person.alias(name, newname) #Går in i objectet person till methoden och skickar med varieblernas värden
                
            elif n[0] == "change":      #Om den första inputen = index 0 är likadan som strängen gör detta...
                    name     = n[1]         #Sätter variabeln till input 2
                    number   = n[2]         #Sätter variabeln till input 3
                    person.change(name, number) #Går in i objectet person till methoden och skickar med varieblernas värden                
                
            elif n[0] == "save":        #Om den första inputen = index 0 är likadan som strängen gör detta...
                    filnamn    = n[1]       #Sätter variabeln till input 2
                    person.save(filnamn)    #Går in i objectet person till methoden och skickar med varieblernas värden
                
            elif n[0] == "load":        #Om den första inputen = index 0 är likadan som strängen gör detta...
                    filnamn    = n[1]       #Sätter variabeln till input 2
                    person.load(filnamn)    #Går in i objectet person till methoden och skickar med varieblernas värden              
                
            elif n[0] == "quit":        #Om den första inputen = index 0 är likadan som strängen gör detta...
                    print("exiting...")
                    exit()
            else:
                print("Invalid input...")
    # ------------- Prompt slut -------------#
telefonbok.prompt()