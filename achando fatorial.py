print(30 * "-")
numero = int(input("Insira um numero: "))
fatorial = 1

if numero < 0:
    print("Não existe fatorial de numeros negativos")
elif numero == 0: 
    print("O fatorial de {numero} é 1")
else:
    for x in range(1,numero+1):
        fatorial = fatorial * x 
print(f"O fatorial de {numero} é: {fatorial} ")
print(30 * "-")
