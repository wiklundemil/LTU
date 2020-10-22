#Skriv ett program som skriver ut en multiplikationstabell för ett tal, t.ex. "3:ans" tabell från 0 till 9. Utskriften ska bli som till höger.
#Skriv programet så att det är enkelt att ändra 3:an till ett annat tal.
num1 = 3
num2 = [0,1,2,3,4,5,6,7,8,9,10]
for number in num2:
    result = num1*number
    print(num1,"*",number,"=",result)