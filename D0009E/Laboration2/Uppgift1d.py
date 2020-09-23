def tvarsumman2(tal):
    lista_enskilda_tal = []
    while tal > 0:
        lista_enskilda_tal.append(tal % 10)         #Lägger till resten från "tal" % 10 och lägger till den i listan.
        tal = (tal - tal % 10) // 10                #Formeln för att få talet från exempelvis 100 till 10. Tar bort sista siffran ut tal.
    print(sum(lista_enskilda_tal)) 
tvarsumman2(1234)