#-------------------Telefonboken------------------------#
class telefonbok:
    def __init__(self):
        self.dictionary = {}
    # -------------- Metoder ---------------#
    def add(self, name, number):
        self.dictionary[name] = number
    def lookup(self, name):
        for obj in self.dictionary:
            if obj == name:
                print("Number:", self.dictionary[obj])
            else: 
                print("Name does not exist in list...")
    # -------------- Metoder slut ---------------#
    
    # ------------- Prompt -------------#
    def prompt():
        person = telefonbok()
        print("Commands:","add","lookup","alias","change","save","load","quit")
        print("Radmall: [command], [name], [number].")
        while True:
            n = input("telebok>").split()
            if n[0] == "add":
                name = n[1]
                number = n[2]
                person.add(name, number)
                print("Added")
            elif n[0] == "lookup":
                name = n[1]
                person.lookup(name)
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
                exit()
                print("quit")
            else:
                print("Invalid input...")
    # ------------- Prompt slut -------------#
telefonbok.prompt()