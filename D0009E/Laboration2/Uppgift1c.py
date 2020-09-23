def tvarsumman(tal):
    if tal != 0:
        n1 = ((tal % 10) + tvarsumman(tal // 10))  
        return n1 #returnerar vi n1 kommer det se ut på följande när vi är i mitten 
                  #av rekursionen: return(3+2+1) + return 0.
                  #Detta kommer alltså att bli: return 6 + 0
    else:
        return 0


def tvarsumman2(tal):
    lista_enskilda_tal = []
    while tal > 0:
        lista_enskilda_tal.append(tal % 10)         #Lägger till resten från "tal" % 10 och lägger till den i listan.
        tal = (tal - tal % 10) // 10                #Formeln för att få talet från exempelvis 100 till 10. Tar bort sista siffran ut tal.
    return(sum(lista_enskilda_tal)) 
import d0009e_lab2_sumTest



