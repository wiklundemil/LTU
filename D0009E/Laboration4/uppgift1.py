#-------------------Telefonboken------------------------#
class telefonbok:
    name = None
    number = None
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.dictionary = {} 
    def info(self):
        return 'Number: {}'.format(self.number) #Denna rad bestämmer vad som ska printas ut när info functionen anropas.
    # -------------- Metoder ---------------#
    def add(self):
        print(name, number)
        

        
    # -------------- Metoder slut ---------------#
    
    # ------------- Prompt -------------#
    def menu():
        print("Commands:","add","lookup","alias","change","save","load","quit")
        print("Radmall: [command], [name], [number].")
        while True:
            n = input("Skriv här:").split()
            if n[0] == "add":
                name = n[1]
                number = n[2]
                person = telefonbok(name, number)
                print("Added")
            elif n[0] == "lookup":
                name = n[1]
                number = n[2]
                print(person)
            elif n[0] == "alias":
                name = n[1]
                number = n[2]
            elif n[0] == "change":
                print("changed")
            elif n[0] == "save":
                name = n[1]
                number = n[2]
            elif n[0] == "load":
                name = n[1]
                number = n[2]
            elif n[0] == "quit":
                print("quit")
            else:
                print("Invalid input...")
    # ------------- Prompt slut -------------#
telefonbok.menu()