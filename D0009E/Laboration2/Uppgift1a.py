def bounce(n):     
    if n==0:
        print(n)    #Påvägen tillbaka kommer den att printa ut alla "sparade" värden av n i det här fallet, 1,2,3 i just den ordningen.
    else: 
        print(n)
        bounce(n-1) 
        print(n)          
import d0009e_lab2_bounceTest

# 1a 1b 2a 2b inte klara