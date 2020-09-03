def cost(loan_amount, years, yearly_interest):                                #Här skapar vi en funktion som erhåller variablerna "loan_amount", "years", "yearly_interest."
    cost=(loan_amount+(years+1)*(loan_amount*yearly_interest)/2)              #Detta är formeln för att räkna ut kostnaden.
    return cost                                                               #return ger oss möjligheten att använda variabeln cost vidare. 


loan_amount = int(input("Sriv in det lånade beloppet:"))                      #Frågar om vad det lånade beloppet är. Via input() sätter man variabeln.
years = int(input("skriv in antal år för återbetalning:"))                    #Samma som ovan.
yearly_interest = float(input("Skriv in den årliga räntesatsen:"))            #Samma som ovan.


result = cost(loan_amount, years, yearly_interest)                            #Skapar variabeln "result" för att kunna spara ned värdet man får när man kallar cost-funktionen.
print("Den totala kostnaden efter",years,"år är "+ str(result) +"kr.")        #Skriver ut hur många år i texten samt omvandlar "result" värdet till en string. 

input("Klicka enter för att avsluta.")                                        #Om man kör detta i shell så kommer programmet avslutas. Därav input() för att stanna upp programmet.
