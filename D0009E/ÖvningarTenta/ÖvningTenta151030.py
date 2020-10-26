#Uppgift 1a Kommer följande program att termingera? SVAR: NEJ Loopen kommer aldrig att terminerpga utav att i alltid kommer vara större eller lika med 0. Därav ingen termingering. 
# i=0 
# while i>=0:
#     if i<1: 
#         continue    
#     i = i+1 


#Uppgift 1b Vilken utskrift ger följande program? SVAR: Olle för att längden av a är 2 och c är 2 och om 2 == 2 då printar den Olle. Därefter går den itne vidare pga av att den gick in i if-satsen.
# a=[["a","b"],["c"]]
# b="c"
# c=2
# if len(a) == c:
#     print("Olle")
# elif len(a+[[b]])<c and c>0:
#     print("aria")
# else:
#     print("Nej")

#Uppgift 1c Vilken utskrift ger följande program? SVAR: -543- Kommer att skrivas ut för att st i for loopen kommer att bli = str(5,4,3) + st.
# s=range(3,6)
# st ="-"
# for c in s:
#     st = str(c)+st
# print("-"+st)


#Uppgift 1d Vad händer när följande kod exekveras (Om det blir fel, varför blir det fel? Om det blir rätt, vilket värde får s?) SVAR: s = int(45.2) + float(4). Det blir 49 eftersom det är int. 0.2 klipps bort för det är float.
# s=float(int("4"+"2")+0.2)+int("3")
# s=int(s)+float("4")
# print(s)

#Uppgift 2 Någon har skrivit en funktion, cumulsum(ls), som är tänkt att ta en lista som parameter och uppdatera listan på följande sätt: elementet 
#på position n i den uppdaterade listan ska innehålla summan av alla element från position 0 till och med n från den ursprungliga listan. M.a.o. 
# varje tal i listan ska vara summan av alla talen från början fram till det talet.
#Programeraren kom fram till följande:
#def cumulsum(ls):
  #i=0
  #while i <=len(ls):
  #   ls[i] = ls[i] + ls[i-1]
  #return i
#SVAR:
# def cumulsum(ls):
#   print("From:",ls)
#   i=1
#   while i <len(ls):
#     ls[i] = ls[i] + ls[i-1]
#     i = i+1
#   else:
#     return ls
# ls=[1,2,3,4]
# print("To:",cumulsum(ls))

#Uppgift 3
#SVAR:
#list1 =[1,7,3]
#list2 =[2,7,3,1]
#list3 =[2,7,3,1] list 2 och pekar på samma lista.  

# def updateList(lst,value):
#     if len(lst)>value:
#       lst = lst+[value]
#     return lst
# list1=[1,7,3]
# list2=updateList(list1, list1[0])
# list2[0]=8
# list3=updateList(list2,list2[0])
# list2[0]=2
# print(list1)
# print(list2)
# print(list3)

#Uppgift 4
def filterSpaces(str_arg):
  change = ["\n","\t","\r"," "]
  for char in str_arg:
    if char in change:
      print("Finns i Change")
      str_arg = str_arg.replace(char,"_",1)
  str_arg = str_arg.replace("_","",2)
  return str_arg
 
print(filterSpaces("\n vi\t testar \rlite "))


#Uppgift 5
# def readList_(filename):
#   rList=[]
#   try:
#     f = open(filename,"r")
#     print(filename,"Opened")
#   except Exception:
#     return rList
  
#   lines = f.readlines()
#   for line in lines:
#     for char in line:
#       if char.isdigit() == True: 
#             print("int hittad:", char)
#             number = int(char)
#             rList = rList +[number]
#     print("New line in file...")
#   print("All numbers in text:",rList)  
#   f.close()
#   print(filename,"Closed")

# n = input("Filnamn:")  
# readList_(n)

