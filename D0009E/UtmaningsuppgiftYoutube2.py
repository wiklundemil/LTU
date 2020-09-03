#Skriv ett program som innehåller en lista med dina favoritmaträtter. Programmet ska fråga efter en maträtt som den lägger till i din lista av favoriter. Ledtråd: input


lista_favorite_foods = ["Blomkålspasta", "Kyckling med jordnötssmör", "Bastard Burgers"] #Skapar en lista med favorit måltider.


print("Dessa är mina favorit måltider",lista_favorite_foods) #Skriver ut i terminalen vilka mina favoritmåltider är.


another_favorite = input("Skriv en till favorit:") #Frågar efter ytterligare en favoritmåltid. 


lista_favorite_foods.append(another_favorite) #Lägger till ytterligare en till favoritmåltid i listan av favoriter. 


print(lista_favorite_foods) #Printar ut den uppdaterade listan. 