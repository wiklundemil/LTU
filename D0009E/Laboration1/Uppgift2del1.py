def recept_sockerkaka(antal):
    #lista_recept_sockerkaka = ["Ägg","Strösocker","Vanlijsocker","Bakpulver","Vetemjöl","Smör","Vatten"]
    
    #print("Receptet inehåller:",lista_recept_sockerkaka)

    print("Detta recept är för",antal,"Personer")
    intantal = int(antal)                                                 #Gör om "antal" från string till int. 

    egg = round((0.75*intantal))                                          #Om man utgår från att det går 3 ägg på 4 personer får man 0.75 ägg på 1 person.
    white_sugar = round((0.75*intantal))                                  #Om man utgår från att det går 3dl strösocker på 4 personer får man 0.75dl strösocker på 1 person.
    vanila_sugar = round((0.5*intantal))                                  #Om man utgår från att det går 2tsk vaniljsocker på 4 personer får man 0.5tsk vanlijsocker på 1 person.
    bakingsoda = round((0.5*intantal))                                    #Om man utgår från att det går 2tsk bakpulver på 4 personer får man 0.5tsk på 1 person.
    flour = round((0.75*intantal))                                        #Om man utgår från att det går 3dl mjöl på 4 personer får man 0.75dl mjöl på 1 person.
    butter = round((18.75*intantal))                                      #Om man utgår från att det går 75gram smör på 4 personer får man 18.75gram smör på 1 person.
    water = round((0.25*intantal))                                        #Om man utgår från att det går 1dl vatten på 4 personer får man 0.25dl vatten på 1 person.
    
    print("Ägg", egg,"st")
    print("Strösocker", white_sugar,"dl")
    print("Vaniljsocker", vanila_sugar,"tsk")
    print("Bakpulver", bakingsoda,"tsk")
    print("Vetemljöl", flour,"dl")
    print("Smör", butter,"g")
    print("Vatten", water,"dl")

#---Här börjar programmet där man ser det i terminalen.---#
antal_personer = input("Hur många personer vill du baka för?")          #Här bestämms hur många personer som man vill baka för. 
recept_sockerkaka(antal_personer)
print()