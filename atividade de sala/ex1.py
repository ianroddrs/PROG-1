#atividade 1
lista = range(2, 1 + int(input("Verificar números primos até: ")))
for i in lista:
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i)