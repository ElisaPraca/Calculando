'''
Descobrindo numeros primos 
7/1 %  = 0
'''
print(30 * "_") 
numero = int(input("Insira um numero para descobrir se é um numero primo:"))

if numero > 1:
    for x in range(2,numero):
        if (numero % x) == 0:
            print("Esse NÃO é um numero primo")
            break
    else: 
        print("Esse numero é primo")
else: 
    print("Esse NÃO é um numero primo")  
print(30 * "_")    
