#-------------------Telefonboken------------------------#
class telefonbok:
    def __init__(self):
        self.dictionary = {}            #dictionary
        self.dictionaryAlias = {}       #dictionary av aliasen
    # -------------- Metoder ---------------#
    def add(self, name, number):
        if name in self.dictionary or number in self.dictionary.values(): #Kontrollerar om nummer eller name finns som key eller value...
            print("Namn eller Nummer existerar redan")
        else: 
             self.dictionary[name] = number  #lägger till i dictionary en nyckel name och sitt value number. Värdena tas från parametern


    def lookup(self, name):
        if name in self.dictionary:   
            print(self.dictionary[name])        #Skriv ut value av nyckeln name
        else:
            if name in self.dictionaryAlias:    #om name finns i dictionaryAlias 
                while name in self.dictionaryAlias: #Startar en loop där man kollar upp det orginella namnet.
                    name = self.dictionaryAlias[name]   #Eftersom dictionaryAlias pekar på föregående namn ex om Emil har value 0709840002. Sätter man ett alias på Emil blir följande alias Emil David i dictionaryAlias lika med {David : Emil}  alias pekar på föregående namn
                print(self.dictionary[name])    #Printar ut value från nyckeln name ur dictionary

    def alias(self, name, newname):
        if name not in self.dictionary:
            if name in self.dictionaryAlias:
                self.dictionaryAlias[newname] = name
            else:
                print("name not found or duplicated name")
        else:
            if name in self.dictionary and newname in self.dictionary:
                print("name not found or duplicated name")               
            else:
                self.dictionaryAlias[newname] = name

    def change(self, name, number):
        if name not in self.dictionary and name not in self.dictionaryAlias:
            print("not found")
        else:
            if name in self.dictionaryAlias or name in self.dictionary:
                while name in self.dictionaryAlias: #Startar en loop där man kollar upp det orginella namnet.
                    name = self.dictionaryAlias[name]   #Eftersom dictionaryAlias pekar på föregående namn ex om Emil har value 0709840002. Sätter man ett alias på Emil blir följande alias Emil David i dictionaryAlias lika med {David : Emil}  alias pekar på föregående namn
                self.dictionary[name] = number            

    def save(self, filnamn):
        fil = open(filnamn, "w")  #Öppnar en ny fil för skrivning
        for obj in self.dictionary: # för varje object i dictionary 
            values = self.dictionary[obj]   #sätter variabeln values till dictionaryts value av dictionaryts nycklar (obj). 
            fil.write(values + ";"+ obj+"\n") #Skriver i filen Nummer + ; + Namn
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