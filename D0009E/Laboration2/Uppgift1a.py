def bounce(n, nreturn): 
    if n == 0:
        rebounce(n, nreturn)
    else:
        print(n)
        bounce(n-1, nreturn) 

def rebounce(n, nreturn):   
    if n == nreturn:        #iterationen körs tills det når värdet av nreturn, vilket är det oförändrade orginella värdet av n.
        print(n)
        print("Bounce complete")    
    else: 
        print(n)
        rebounce(n+1, nreturn)

n = int(input("Skriv en siffra:"))
nreturn = n         #nreturn sätts samma som n men nreturn förblir oförändrat i syfte att ha kvar det orginella talet.
bounce(n,nreturn)   