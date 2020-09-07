def recept(antal):
    #lista_recept_sockerkaka = ["Ägg","Strösocker","Vanlijsocker","Bakpulver","Vetemjöl","Smör","Vatten"]
    #print("Receptet inehåller:",lista_recept_sockerkaka)

    print("Detta recept är för",antal,"Personer.")
    print()
    intantal = int(antal)                                                 #Gör om "antal" från string till int. 

    egg = round((0.75*intantal))                                          #Om man utgår från att det går 3 ägg på 4 personer får man 0.75 ägg på 1 person.
    white_sugar = (0.75*intantal)                                #Om man utgår från att det går 3dl strösocker på 4 personer får man 0.75dl strösocker på 1 person.
    vanila_sugar = (0.5*intantal)                                  #Om man utgår från att det går 2tsk vaniljsocker på 4 personer får man 0.5tsk vanlijsocker på 1 person.
    bakingsoda = (0.5*intantal)                                   #Om man utgår från att det går 2tsk bakpulver på 4 personer får man 0.5tsk på 1 person.
    flour = (0.75*intantal)                                     #Om man utgår från att det går 3dl mjöl på 4 personer får man 0.75dl mjöl på 1 person.
    butter = (18.75*intantal)                                      #Om man utgår från att det går 75gram smör på 4 personer får man 18.75gram smör på 1 person.
    water = (0.25*intantal)                                        #Om man utgår från att det går 1dl vatten på 4 personer får man 0.25dl vatten på 1 person.
    
    print("Ägg", egg,"st")
    print("Strösocker", white_sugar,"dl")
    print("Vaniljsocker", vanila_sugar,"tsk")
    print("Bakpulver", bakingsoda,"tsk")
    print("Vetemljöl", flour,"dl")
    print("Smör", butter,"g")
    print("Vatten", water,"dl")


def tidblanda(antal):                                          #Detta är funktionen som beräknar tiden för att blanda scokerkakan.
    intantal = int(antal)
    tid_blanda = ((intantal*1) + 10)
    return tid_blanda


def tidgrada(antal):                                           #Detta är funktionen som beräknar tiden för att grädda sockerkakan.
    intantal = int(antal)
    tid_grada = ((intantal*3) + 30)
    return tid_grada


def sockerkaka(antal):                                         #Detta är huvudfunktionen.
    recept(antal)

    tid_totalt = tidblanda(antal) + tidgrada(antal)
    print()
    print("Det tar totalt så här lång tid att genomföra receptet:",tid_totalt,"min")


#---Här börjar programmet där man ser det i terminalen.---#
antal = input("Hur många personer vill du baka för?")          #Här bestämms hur många personer som man vill baka för. 
sockerkaka(antal)                                              #Detta är huvudfunktionen som kallar på functionen tidgrada och tidblanda.
print()


