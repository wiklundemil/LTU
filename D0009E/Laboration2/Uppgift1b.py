def bounce2(n, nreturn):
    while n > 0:
        print(n)
        n = (n-1)
    if n == 0:
        rebounce2(n, nreturn)


def rebounce2(n, nreturn):
    while n < nreturn:     
        print(n)      
        n = (n+1)
    if n == nreturn:       #iterationen körs tills det når värdet av nreturn, vilket är det oförändrade orginella värdet av n.
        print(n)
        print("Bounce complete")


n = int(input("Skriv en siffra:"))
nreturn = n         #nreturn sätts samma som n men nreturn förblir oförändrat i syfte att ha kvar det orginella talet.
bounce2(n, nreturn)