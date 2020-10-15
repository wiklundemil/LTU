#-------------------Telefonboken------------------------#
class telefonbok:
    def __init__(self):
        self.dictionary = {}            #dictionary
        self.dictionaryAlias = {}       #dictionary av aliasen
    # -------------- Metoder ---------------#
    def add(self, name, number):
        self.dictionary[name] = number  #lägger till i dictionary en nyckel name och sitt value number. Värdena tas från parametern
    

    def lookup(self, name):
        if name in self.dictionary:             #Om name finns i dictionary
            print(self.dictionary[name])        #Skriv ut value av nyckeln name
        else:
            if name in self.dictionaryAlias:    #om name finns i dictionaryAlias 
                while name in self.dictionaryAlias: #Startar en loop där man kollar upp det orginella namnet.
                    name = self.dictionaryAlias[name]   #Eftersom dictionaryAlias pekar på föregående namn ex om Emil har value 0709840002. Sätter man ett alias på Emil blir följande alias Emil David i dictionaryAlias lika med {David : Emil}  alias pekar på föregående namn
                print(self.dictionary[name])    #Printar ut value från nyckeln name ur dictionary
            else: 
                print("Number:", self.dictionary[name]) #Om name redan är det orginella printar den ut value ur dictionary 


    def alias(self, name, newname):
        for obj in self.dictionary:    #För varje obj i dictionary
            if obj == name:            #Kolla om obj är lika med det namnet som fås från parametern
                self.dictionaryAlias[newname] = obj #Om det ovan är sant sätts det nya namnet in som key i dictionaryAlias och får värdet av föregående orginalnamn ex {David : Emil} Man kan säga att David hänsvisar till Emil
            else:                      #Om inte
                self.dictionaryAlias[newname] = name    #sätter man in det nya namnet som key i dictionaryAlias och name som value


    def change(self, name, number):
        if name in self.dictionaryAlias:        #Om nam som fås från parametern
            while name in self.dictionaryAlias:     #Medans name finns i dictionaryAlias
                name = self.dictionaryAlias[name]   #Skapar en snurra där man går till orginal namnet som aliaset skapades ifrån från början.
            updatednumber = self.dictionary[name] = number  #Denna använder orginalnanet som letas upp som i raden ovan visar och sätter det nya numret på orginalnamnet
            print("New number:",updatednumber)
        else: 
            updatednumber = self.dictionary[name] = number  #Om namnet som ska uppdateras är ett orginal namn och inte ett alias ändrar man orginalnamnets value (number) till det nya number som fås från parametern
            print("New number:",updatednumber)
    
    
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
            if len(n) >= 2:                 #Split skapar en lista med antalet "inputs" ex, input 1 input 2 man kan inte skriva in mindre än 2 inputs
                if n[0] == "add":           #Om den första inputen = index 0 är likadan som strängen gör detta...
                    name    = n[1]          #Sätter variabeln till input 2
                    number  = n[2]          #Sätter variabeln till input 3
                    person.add(name, number)#Går in i objectet person till methoden och skickar med varieblernas värden
                    print("Added")
                
                elif n[0] == "lookup":      #Om den första inputen = index 0 är likadan som strängen gör detta...
                    name    = n[1]          #Sätter variabeln till input 2
                    person.lookup(name)
                
                elif n[0] == "alias":       #Om den första inputen = index 0 är likadan som strängen gör detta...
                    name    = n[1]          #Sätter variabeln till input 2
                    newname = n[2]          #Sätter variabeln till input 3
                    person.alias(name, newname) #Går in i objectet person till methoden och skickar med varieblernas värden
                    print("Added")
                
                elif n[0] == "change":      #Om den första inputen = index 0 är likadan som strängen gör detta...
                    name     = n[1]         #Sätter variabeln till input 2
                    number   = n[2]         #Sätter variabeln till input 3
                    person.change(name, number) #Går in i objectet person till methoden och skickar med varieblernas värden
                    print("changed")
                
                elif n[0] == "save":        #Om den första inputen = index 0 är likadan som strängen gör detta...
                    filnamn    = n[1]       #Sätter variabeln till input 2
                    person.save(filnamn)    #Går in i objectet person till methoden och skickar med varieblernas värden
                elif n[0] == "load":        #Om den första inputen = index 0 är likadan som strängen gör detta...
                    filnamn    = n[1]       #Sätter variabeln till input 2
                    person.load(filnamn)    #Går in i objectet person till methoden och skickar med varieblernas värden              
                elif n[0] == "quit":        #Om den första inputen = index 0 är likadan som strängen gör detta...
                    exit()
                    print("quit")
                
                else:
                    print("Invalid input...")
            else: 
                print("Not valid...")
    # ------------- Prompt slut -------------#
telefonbok.prompt()