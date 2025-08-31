n = int(input("Digite um número para calcular o fatorial :"))
if n < 0:
    print("Fatorial não definido para números negativos.")
elif n == 0 or n == 1:
    n = 1
else:
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
        print(resultado)
