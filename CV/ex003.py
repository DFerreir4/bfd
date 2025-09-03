opcao = int(input("Digite uma das opções: [1 - soma][2 - subtração] [3 - multiplicação][4 - divisão]"))



if opcao == 0 or opcao == "":
     print("Você não digitou nenhuma das opções. Reinicie o sistema.")
elif opcao == 1:
    n1 = float(input("Digite o primeiro número : "))
    n2 = float(input("Digite o segundo número : "))
    print(f"Você escolheu [SOMA]. O total de {n1} + {n2} = {n1+n2}")
elif opcao == 2:
     n1 = float(input("Digite o primeiro número : "))
     n2 = float(input("Digite o segundo número : "))
     print(f"Você escolheu [SUBTRAÇÃO]. O total de {n1} - {n2} = {n1-n2}")
elif opcao == 3:
     n1 = float(input("Digite o primeiro número : "))
     n2 = float(input("Digite o segundo número : "))
     print(f"Você escolheu [MULTIPLICAÇÃO]. O total de {n1} X {n2} = {n1*n2}")
elif opcao == 4:
    n1 = float(input("Digite o primeiro número : "))
    n2 = float(input("Digite o segundo número : "))
    print(f"Você escolheu [DIVISÃO]. O total de {n1} / {n2} = {n1/n2}")
