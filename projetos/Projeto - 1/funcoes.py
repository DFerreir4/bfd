def cadastro_aluno():  
    while True:
            numero = int(input("Deseja cadastrar um aluno e as notas? [1 - SIM],[0 - NÃO]"))

            if numero != 0:    
                nome = str(input("Digite seu o nome do aluno : "))
                idade = int(input(f"Digite a idade de {nome} : "))

                lista = []
                for i in range(1,4):
                    nota = float(input(f"Digite a {i}° nota : "))
                    lista.append(nota)

                media = (lista[0]+lista[1]+lista[2])/3
                if media >= 7 :
                      status = "APROVADO"
                else: status = "REPROVADO"

                cadastro = {}
                cadastro["nome"] = nome
                cadastro["idade"] = idade
                cadastro["nota1"] = lista[0]
                cadastro["nota2"] = lista[1]
                cadastro["nota3"] = lista[2]
                cadastro["media"] = f"{media:,.2f}"
                cadastro["status"] = status

                for chave, valor in cadastro.items():
                    print(f"{chave}: {valor}")
                print("__________________________________")

            elif numero == 0:
                print(f"Operação finalizada!")
                break
    

   