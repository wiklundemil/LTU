class telefonbok:
    def __init__(self):
        self.dictionary = {}
        self.dictionary["Emil"] = 1
        self.dictionaryAlias = {}
    def alias(self):
        user_input1 = "Emil"
        user_input2 = "David" 

        self.dictionaryAlias[user_input2] = user_input1
        print("Namn är nyckel, Nummer är value",self.dictionary)
        print("Alias är nyckel, Namn är value",self.dictionaryAlias) # David är alias för namnet Emil 
        
person = telefonbok()
person.alias()