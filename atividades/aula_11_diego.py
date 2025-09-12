'''#1 Crie uma função chamada `dobrar` que recebe um número 
como parâmetro e retorna o dobro desse valor. Teste a função 
com o número 5.
'''

def dobrar(numero): #A função solicita um valor como pâmetro.
    return f"O dobro de {numero} é {numero*2}"
    '''Após executar a função com um argumento, 
       ela ira retornar o valor em dobro.'''

dobrar(5)

#___________________________________________________________________________________________________________________________________________________

'''#2 Crie uma classe `Livro` com os atributos `titulo` e `autor`. Adicione um método `exibir_dados` que retorna uma string no formato: `"Título: [titulo], Autor: [autor]"`. Instancie um livro com título "1984" e autor "George Orwell", e chame o método.
'''

class Livro:
    #foi criado o construtor com dois atributos: titulo e livro
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    #exibir dados é um metodo criado para exibir os atributos que foram pedidos. Obs: Não coloquei return por conta de formatação
    def exibir_dados(self):
        print(f"Titulo : [{self.titulo}]\n Autor : [{self.autor}]")

l = Livro("1984","George Orwell")
l.exibir_dados()

#___________________________________________________________________________________________________________________________________________________

'''3 Dada a classe `Carro` abaixo:
Crie um objeto `meu_carro` com modelo "Fusca" e cor "Azul". Em seguida, altere a cor para "Vermelho" e imprima o novo valor do atributo `cor`.'''
class Carro:

    def __init__(self,modelo,cor):
        self.modelo = modelo
        self.cor = cor

meu_carro = Carro("Fusca","Azul")
#até esse ponto a cor do carro era azul.
meu_carro.cor = "Vermelho"
#O atributo cor foi alterado ao receber um novo valor. Antes Azul e agora Vermelho.

print(f"Modelo do carro : [{meu_carro.modelo}]\n Cor do carro : [{meu_carro.cor}]")

#___________________________________________________________________________________________________________________________________________________

'''4 Funções com Múltiplos Parâmetros
Escreva uma função `calcular_imc` que recebe peso (kg) e altura (m) e retorna o IMC (peso / altura²). Se o IMC for:
- < 18.5: retorne "Abaixo do peso"
- 18.5 a 24.9: retorne "Peso normal"
- 25 a 29.9: retorne "Sobrepeso"
- ≥ 30: retorne "Obesidade"
Teste com peso 70 kg e altura 1.75 m.'''

def calcular_imc(peso,altura):
    
    imc = peso/(altura**2)

    if imc < 18.5:
        return f"Abaixo do Peso! Seu IMC foi : {imc:,.2f}"
    elif imc >= 18.5 or imc < 24.9:
        return f"Peso Normal! Seu IMC foi : {imc:,.2f}"
    elif imc == 25 or imc <= 29.9:
        return f"Sobrepeso! Seu IMC foi : {imc:,.2f}"
    elif imc >= 30:
        return f"Obesidade! Seu IMC foi : {imc:,.2f}"
    

calcular_imc(70,1.75)

#___________________________________________________________________________________________________________________________________________________

'''5 Métodos que Modificam Atributos
Crie uma classe `Conta` com atributo `saldo` (inicializado como 0). Adicione métodos:
- `depositar(valor)`: adiciona o valor ao saldo
- `sacar(valor)`: subtrai o valor do saldo (apenas se houver saldo suficiente)
Crie uma conta, deposite 100, saque 30 e imprima o saldo final.'''

class Conta:

    def __init__(self,saldo:float=0.0):
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor
        print(f"+ Credito : R$ {valor:.2f}")

    def sacar(self,valor):
        #O if abaixo é para sacar o valor que ele tem no saldo. Caso ele tente sacar um valor maior que o do saldo, sua conta vai estar negativa. Então é impedido que seja feita a ação.
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print( f"- Debito : R$ {valor:.2f}")
            else:
                return f"Sua conta está com o saldo R$ {self.saldo:.2f}. Não é possivel sacar o valor R$ {valor:.2f}."

c = Conta()
print("-"*30) #Os print("-"*30) foi utilizado para formatação da saída. Ele multiplica 30 vezes a string
print(f"Saldo Inicial: {c.saldo}")
print("-"*30)
c.depositar(100)
c.sacar(30)
print("-"*30)
print(f"Saldo Total: R$ {c.saldo:,.2f}")
print("-"*30)

#___________________________________________________________________________________________________________________________________________________

'''6 Interação entre Objetos
Crie uma classe `Pedido` com atributos `produto` e `quantidade`. Crie uma classe `Cliente` com atributo `nome` e um método `fazer_pedido(produto, quantidade)` que retorna um objeto `Pedido`. Faça um cliente "João" fazer um pedido de "Notebook" com quantidade 2'''

class Pedido:
    
    def __init__(self,produto_p,quantidade_p):
        self.produto_p = produto_p
        self.quantidade_p = quantidade_p

class Cliente:

    def __init__(self,nome):
        self.nome = nome
    
    def fazer_pedido(self,produto,quantidade):
        #o if foi criado para não deixar o campo em branco ou zerado.
        if (produto == "" or produto == 0) or (quantidade == "" or quantidade == 0):
            print("Produto ou quantidade com valor incorreto")
        else: print(f"Cliente : {self.nome}")
        print(f"Produto : {produto} // Quantidade : {quantidade}")
        
      
print("-"*30)
c = Cliente("João")
p = Pedido("Notebook",2)
c.fazer_pedido(p.produto_p,p.quantidade_p) #instanciando Cliente e inserindo os dados da instancia de Pedido no metodo fazer_pedido
print("-"*30)

#___________________________________________________________________________________________________________________________________________________

'''7 Crie uma classe `Ponto` com atributos `x` e `y`. Implemente o método `__str__` para retornar `"(x, y)"` e o método `__add__` para permitir a soma de dois pontos (soma das coordenadas). Teste criando dois pontos (1, 2) e (3, 4), somando-os e imprimindo o resultado.'''

class Ponto:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,novo):
        #Retorna um novo objeto Ponto com as cordenadas somadas
        return Ponto(self.x + novo.x, self.y + novo.y)
    
    def __str__(self):
        #define o que vai ser exibido na saída.
        return f"({self.x},{self.y})"
    
p1 = Ponto(1,2) #Foi utilizado duas instancias para fazer a soma do do metodo __add__
p2 = Ponto(3,4)

total_pontos = p1 + p2

print(total_pontos)

#___________________________________________________________________________________________________________________________________________________

'''8 Classe com Lista de Objetos
Crie uma classe `Turma` com atributo `alunos` (lista vazia). Adicione métodos:
- `adicionar_aluno(aluno)`: adiciona um objeto `Aluno` à lista
- `media_turma()`: calcula a média das notas de todos os alunos (cada aluno tem uma lista de notas)
Use a classe `Aluno` da aula. Crie 3 alunos com notas [8,7,9], [6,5,7], [9,8,9], adicione-os à turma e calcule a média geral.'''

class Turma:

    def __init__(self):
        self.alunos = {}
        #A lista foi feita através de um dicionário.
    def adicionar_aluno(self,aluno,nota):
        if aluno != self.alunos:
            #aluno for diferente de self.alunos, vai ser criado uma lista para inserir as notas nessa lista
            self.alunos[aluno] = []
            self.alunos[aluno].extend(nota)
            print(f"Notas {nota} do aluno {aluno} foi adicionado com sucesso!")
    
    def media_turma(self):
        todas_as_notas = []
        #outra lista criadas de todas as notas de todos os alunos criados
        for notas in self.alunos.values():
            todas_as_notas.extend(notas)

        #somando todas as notas
        soma_notas = sum(todas_as_notas)
        #pegando a quantidade de tonas que foram inseridas em todas_as_notas
        qtd_notas = len(todas_as_notas)
        #calculo da media dividindo a soma_notas pela qtd_notas
        media = soma_notas / qtd_notas

        return media

t = Turma()
t.adicionar_aluno("Maria",[8,7,9])
t.adicionar_aluno("José",[6,5,7])
t.adicionar_aluno("João",[9,8,9])

media_geral = t.media_turma()

print(f"média de todas as notas da turma é: {media_geral:.2f}")

#___________________________________________________________________________________________________________________________________________________

'''9 Composição de Objetos
Crie uma classe `Motor` com atributo `potencia`. Crie uma classe `Carro` com atributos `modelo` e `motor` (objeto da classe `Motor`). Adicione um método `exibir_detalhes` que retorna `"Modelo: [modelo], Motor: [potencia] CV"`. Crie um motor de 150 CV, um carro "Ferrari" com esse motor, e exiba os detalhes. '''

class Motor:

    def __init__(self,potencia):
        self.potencia = potencia

class Carro:

    def __init__(self,modelo,motor):
        self.modelo = modelo
        self.motor = motor
        

    def exibir_detalhes(self):
        #Foi inserido o dado potencia da classe Motor em self.motor.potencia
        return f"Modelo: {self.modelo}, Motor: {self.motor.potencia} CV"
    
m = Motor(150)
c = Carro("Ferrari",m)
c.exibir_detalhes() 

#___________________________________________________________________________________________________________________________________________________

'''10 Sistema de Biblioteca
Crie um sistema com as classes:
- Livro: atributos `titulo`, `autor`, `disponivel` (True por padrão)
- Biblioteca: atributo `livros` (lista de objetos `Livro`)
- Usuario: atributo `nome` e método `emprestar_livro(biblioteca, titulo)` que:
- Procura o livro na biblioteca
- Se disponível, altera `disponivel` para False e retorna `"Livro emprestado com sucesso!"`
- Senão, retorna `"Livro indisponível!"`
Teste criando 3 livros, adicionando-os à biblioteca, e um usuário "Ana" emprestando um livro disponível e um indisponível.'''

class Livro:

    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

class Biblioteca:

    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def procurar_livro(self, titulo):
        # Busca case-insensitive pelo título e retorna o primeiro encontrado
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        

class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def emprestar_livro(self, biblioteca, titulo):
        livro = biblioteca.procurar_livro(titulo)
        if livro and livro.disponivel:
            livro.disponivel = False
            return "Livro emprestado com sucesso!"
        else:
            return "Livro indisponível!"

# --- Teste solicitado ---
# Criando a biblioteca e os livros
b = Biblioteca()
l1 = Livro("1984", "George Orwell")
l2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
l3 = Livro("Dom Casmurro", "Machado de Assis", disponivel=False)  # já indisponível

# Adicionando livros à biblioteca
b.adicionar_livro(l1)
b.adicionar_livro(l2)
b.adicionar_livro(l3)

# Usuário Ana tentando emprestar um livro disponível e um indisponível
nome = Usuario("Ana")
resultado1 = ana.emprestar_livro(b,"1984")           # deve emprestar com sucesso
resultado2 = ana.emprestar_livro(b,"Dom Casmurro")  # deve retornar indisponível

print(resultado1)
print(resultado2)

# Mostrar estado final dos livros
for livro in b.livros:
    print(f"{livro.titulo} - disponível: {livro.disponivel}")

#___________________________________________________________________________________________________________________________________________________

'''Desafios extras do slide da aulta 12

3.Expanda o simulador de conta:
● Crie uma lista de contas.
● Permita ao usuário escolher uma conta pelo nome e fazer operações.
4.Desafio:
adicione ao banco um método de juros que aumenta o saldo em 5%'''


class ContaBancaria:

    def __init__(self,titular,saldo:float=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        self.saldo += valor
        print(f"+ Credito : R$ {valor:.2f}")

    def sacar(self,valor):
        #O if abaixo é para sacar o valor que ele tem no saldo. Caso ele tente sacar um valor maior que o do saldo, sua conta vai estar negativa. Então é impedido que seja feita a ação.
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print( f"- Debito : R$ {valor:.2f}")
            else:
                return f"Sua conta está com o saldo R$ {self.saldo:.2f}. Não é possivel sacar o valor R$ {valor:.2f}."

class Banco:
        
        def __init__(self):
            self.contas = []

        def adicionar(self, conta):
            self.contas.append(conta)

        def buscar(self, nome):
            for c in self.contas:
                if c.titular == nome:
                    return c
                
        def aplicar_juros(self):
            for c in self.contas:
                c.saldo *= 1.05  # aumenta 5%

#Foi adicionado dois usuarios
b = Banco()
b.adicionar(ContaBancaria("Ana", 100))
b.adicionar(ContaBancaria("João", 50))

print("-"*30)
print("-"*30)
c = b.buscar("Ana")
print(f"Titular: {c.titular}")
c.depositar(50)
c.sacar(30)
b.aplicar_juros()
print("+ Juros de 5%")
print(f"Saldo Total : {c.saldo}")
print("-"*30)
print("-"*30)
c = b.buscar("João")
print(f"Titular: {c.titular}")
c.depositar(50)
c.sacar(30)
b.aplicar_juros()
print("+ Juros de 5%")
print(f"Saldo Total : {c.saldo}")