n = int(input("Digite um número para exibir números primos : "))

if n < 2:
    print(f"O número [{n}] é primo!")
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            print("não é número primo")
