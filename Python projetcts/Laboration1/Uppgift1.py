def cost(loan_amount, years, yearly_interest):
    cost=(loan_amount+(years+1)*(loan_amount*yearly_interest)/2)
    return cost


loan_amount = int(input("Sriv in det lånade beloppet:"))
years = int(input("skriv in antal år för återbetalning:"))
yearly_interest = float(input("Skriv in den årliga räntesatsen:"))


#loan_amount = 50000
#years = 10
#yearly_interest = 0.03


result = cost(loan_amount, years, yearly_interest)
print("Den totala kostnaden efter",years,"år är "+ str(result) +"kr.")

input("Klicka enter för att avsluta.")
