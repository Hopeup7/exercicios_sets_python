#Questão 2️⃣6
#Crie um conjunto com 5 números inteiros e imprima-o.
conjuntos = {1, 2, 3, 4, 5, 6, 7,}
print(conjuntos)
#aqui eu criei um conjunto com 7 elementos do tipo inteiro.

#Questão 2️⃣7
#Adicione os elementos 10, 20, 30 a um conjunto e imprima o resultado.
conjuntos.add(10)
conjuntos.add(20)
conjuntos.add(30)
print(conjuntos)
#aqui eu criei um conjunto através do método .add() que é pertencente a classe set e adicionei os elementos 10, 20, 30.  

#Questão 2️⃣8
#Remova um elemento específico de um conjunto
conjuntos.discard(6)
conjuntos.remove(4)
conjuntos.discard(6)
conjuntos.remove(4)
print(conjuntos)
# aqui eu removi atraves de dois metodos pertencentes a classe set, o .discard() e .remove(). e quando eu removi novamente com o método.remove(4) ele me gerou um erro : KeyError:, mas foi o keyError porque o keyError é um erro que ocorre por serem hashes, e são tratados como chaves seus elementos.


#Questão 2️⃣9
#Crie um conjunto vazio e adicione elementos dinamicamente com input().
dados = set()
dados = input(f"Adicione 5 elementos separados por virgula").strip().lower().split(", ")#► aqui eu crio uma variael que vai receber um dado do input sendo este dado já modificado em tempo de atribuição, onde ele será convertido para minuscula e retirado os espaços em branco., pois o .strip() um método que remove espaços em branco do inicio e fim de uma string e o lower() converte a string para minuscula. depois, se houvesse duplicats, a conversão de tudo isto em set(), já me precavia isto. no primeiro output veio em forma de lista, pois o .split() separa a string digitada pelo usuario em uma lista de substrings, onde o separador é a virgula e o espaço, operação feita pelo método .spli(", ") 

dados = set()
dados = set(input(f"Adicione 5 elementos separados por virgula\n").strip().lower().split(", "))
print(f" Os elementos que estão na variavel dados são: {dados}") 
# abaixo o output:
# Adicione 5 elementos separados por virgula
# 1, 2, 3, 4, 5
#  Os elementos que estão na variavel dados são: ['1', '2', '3', '4', '5']
# PS C:\Users\Pichau\OneDrive\Área de Trabalho\estudo_conjuntos> & C:/Users/Pichau/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Pichau/OneDrive/Área de Trabalho/estudo_conjuntos/conjuntos.py"
# Adicione 5 elementos separados por virgula
# 1, 2, 32, 5, 32, 2, 2, 4, 5, 1
#  Os elementos que estão na variavel dados são: {'4', '5', '1', '2', '32'}
# PS C:\Users\Pichau\OneDrive\Área de Trabalho\estudo_conjuntos> 

#Questão 3️⃣0
#Faça um programa que converta uma lista com números repetidos em um conjunto, eliminando duplicatas.
#Questão 3️⃣1
#Peça ao usuário para digitar 5 nomes e os armazene em um conjunto sem duplicação.

#► vc me ajudou a concluir e colocar lógica nestes algoritmos abaixo:

def visualizar_conjunto(lista):
    '''Essa função tem por objetivo visualizar o elementos.'''

    print(f"\nOs elementos que vc inseriu são:\n{lista}")
def visualizar_sem_duplicats(lista):
    '''Essa função recebe uma lista e a converte em set para remoção de duplicatas. '''
    sem_duplicatas = list(set(lista))
    sem_duplicatas.sort()
    print(f"Agora sua lista esta sem duplicatas:\n{sem_duplicatas}")
    return sem_duplicatas
def inserção_de_dados(lista):
    '''Essa função vai ser de incremento a lista.'''
    novos_dados = input(f"\nQuais elementos vc quer inserir? (separados por vírgula)\n").strip().lower().split(", ")
    lista.extend(novos_dados)
    
    print(f"\nA lista está assim atualmente:\n{lista}")
    return lista.sort()
def programinha_sem_duplicatas():
    '''aqui eu crio uma função que vai gerar um loop  para que o usuario tenha ciencia de que enquanto ele não confirmar com sair, o loop de inserção vai continuar e adicionr elementos, mas a convesão em set() vai eliminar todas duplicatas. '''
    lista = []
    while True:
        try:
            print("\n🔥 Escolha uma opção abaixo:")
            print("0) Inserir elementos.")
            print("1) Visualizar todas as inserções.")
            print("2) Visualizar lista sem duplicatas.")
            print("3) Encerrar operação.")

            dados = input(f"Digite a opção desejada:\n\U0001f525 ").strip()
                       
            if not dados:
                raise ValueError(f"\U000026a0 Você não digitou nada.")

            elif not dados.isdigit():
                raise ValueError(f"\U000026a0 Digite apenas os números descritos na opção da mensagem principal")
            
            dados = int(dados)

            if dados < 0 and dados > 3:
                raise ValueError(f"\U0000274c Opção inválida. Escolha as opções descritas na mensagem principal.")
        
            elif dados == 3:
                print(f"\n\U0001f44b Até mais.")
                break

            elif dados == 0:
                inserção_de_dados(lista)

            elif dados == 1:
                visualizar_conjunto(lista)

            elif dados == 2:
                visualizar_sem_duplicats(lista)
            
            else:
                raise ValueError(f"|U000026a0 Digite um aopção entre 0 e 3")

        except ValueError as v:
            print(f"\U0000274c Erro: {v}")
        else:
            print(f"A operação funcionou.")
        finally:
            print(f"\U0001f44b Encerrando operação...")
programinha_sem_duplicatas()

# Questão 3️⃣2
# Verifique se um número específico está presente em um conjunto

conjunto = {1, 2, 3, 4, 5}
print(f"O numero 3 está no conjunto:{conjunto}?\n{3 in conjunto}\n")
print(f"O numero 2 está no conjunto:{conjunto}?\n{2 in conjunto}\n")
print(f"O numero 100 está no conjunto:{conjunto}?\n{100 in conjunto}\n")
print(f"O numero 1 está no conjunto:{conjunto}?\n{1 in conjunto}\n")
print(f"O numero 5 está no conjunto:{conjunto}?\n{5 in conjunto}\n")
print(f"O numero 200 está no conjunto:{conjunto}?\n{200 in conjunto}\n")
print(f"O numero 5000 está no conjunto:{conjunto}?\n{5000 in conjunto}\n")


#Questão 3️⃣3
#Crie um conjunto com números de 1 a 10 e remova números ímpares dele.

conjuntos = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for i in conjuntos:
    if i in conjuntos.copy() % 2 == 0:
        print(f"Os numeros divisíveis por 2 são pares.")
    else:
        print(f"Os numeros não são divisíveis por 2, e por isso são ímpares.")
else:
    print(f"Tornando conjuntos novamente em tipo set.\n{set(conjuntos)}")


#Questão 3️⃣4
#Gere um conjunto com os primeiros 20 números primos e exiba-os

def eh_primo(num):
    '''aqui eu crio uma função que vai me gerar os primeiros 20 numeros primos'''
    lista = [x for x in range(2, 20) if (x % 1 and x % x == x or x == 1)] 
    print(f"Estes numeros são primos:\n{lista}")
    return lista
conjunto = range(2, 20)
print(conjunto)


#Questão 3️⃣5
#Peça ao usuário para inserir 10 palavras e exiba apenas as únicas (sem repetição).

palavras = input(f"Digite 10 palavras").lower().split(", ", ",").strip()
print(f"{set(palavras)}")

palavras = input(f"Digite 10 palavras:\n\U0001f525 ").strip().lower().split(", ")
print(f"{set(palavras)}")
# #PS C:\Users\Pichau\OneDrive\Área de Trabalho\estudo_conjuntos> & C:/Users/Pichau/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Pichau/OneDrive/Área de Trabalho/estudo_conjuntos/conjuntos.py"
# Digite 10 palavras:
# 🔥  café, café, pão, pão, chá, chá, leite, leite, bolacha, bolacha, café, café, pão, pão, chá, chá, leite, leite, bolacha, bolacha
# {'café', 'chá', 'pão', 'leite', 'bolacha'}
# PS C:\Users\Pichau\OneDrive\Área de Trabalho\estudo_conjuntos> 


# Questão 3️⃣6
# Crie dois conjuntos e exiba sua união (union())
set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {6, 7, 8, 9, 10}
print(f"\n\U0001f525 A união dos conjuntos é:\n{set.union(set2)}")
#aqui ele uniu os conjuntos, mas 'não' repetiu seus elementos.

# Questão 3️⃣7
# Crie dois conjuntos e exiba sua interseção (intersection()).
set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {6, 7, 8, 9, 10}
print(f"\n\U0001f525 A interseção, ou melhor, os elementos em \"comum\" dos conjuntos são:\n{set.intersection(set2)}")

# Questão 3️⃣8
# Crie dois conjuntos e exiba a diferença (difference()) entre eles
set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {6, 7, 8, 9, 10}
print(f"\n\U0001f525 Os elementos que estão no set e \"não\" no set2 são:\n{set.difference(set2)}")

# Questão 3️⃣9
# Verifique se um conjunto é um subconjunto de outro (issubset())
set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {6, 7, 8, 9, 10}

print(f"\U0001f525 O set é um subconjunto de set2?\n{set.issubset(set2)}")
#isto me retornará false, pois o set que chama a função .issubset() esta querendo somente saber "se" seus elementos são "pertencentes" ao set2, que foi passado como argumento.

# Questão 4️⃣0
# Verifique se um conjunto é um superconjunto de outro (issuperset()).
set = {6, 7, 8, 9, 10}
set2 = {6, 7, 8, 9, 10}

print(f"O set é um superconjunto se set2?\n{set.issuperset(set2)}")
#►  o set que chama a função .issuperset() esta querendo somente saber "se" seus elementos são "pertencentes" ao set2, que foi passado como argumento. esta foi a resposta que vc me gerou.

#Então, quando eu chamo o método .issupersdet() o set que o chama "quer saber se" seus elementos "são pertencentes ao conjunto passado como argumento"?"


# Questão 4️⃣1
# Faça um código que compare dois conjuntos e determine se eles são disjuntos (isdisjoint()).
set = {6, 7, 8, 9, 10}
set2 = {6, 7, 8, 9, 10}
set3 = {11, 12, 13, 14, 15}
set4 = {20, 21, 22, 6, 7}
# Aqui eu vou olicitar um retorno booleano, onde o .isdisjoin() vai me retornar true se forem distintos em totalidade de elementos, ou seja, se forem 'todos' diferentes retornará true, se um set contiver ao menos um elemento igual vai retornar false, porque nãosão disjuntos 
print(f"\U0001f525 Os sets são disjuntos?\n{set.isdisjoint(set2)}")#►true 
print(f"\U0001f525 Os sets são disjuntos?\n{set.isdisjoint(set3)}")#► true, por
print(f"\U0001f525 Os sets são disjuntos?\n{set.isdisjoint(set4)}")#►false, por q
print(f"\U0001f525 Os sets são disjuntos?\n{set4.isdisjoint(set)}")#►false, por que um de seus elementos também é igual a um dos elementos do set. Então, se um dos elementos for igual, o set não é disjunto.


# Questão 4️⃣2
# Crie três conjuntos aleatórios e exiba suas combinações (utilizando union, intersection e difference)
set2 = {6, 7, 8, 9, 10}
set3 = {11, 12, 13, 14, 15, 6, 7, 8}
set4 = {20, 21, 22, 6, 7}

print(f"\n\U0001f525 A união dos conjuntos é:\n{set3.union(set2)}")
print(f"\n\U0001f525 A união dos conjuntos é:\n{set4.union(set3)}")
print(f"\n\U0001f525 A união dos conjuntos é:\n{set2.union(set3)}")
print(f"\n\U0001f525 Os elementos em comum são:\n{set3.intersection(set2)}")#► {6, 7, 8}
print(f"\n\U0001f525 Os elementos em comum são:\n{set2.intersection(set3)}")#► {6, 7, 8}
print(f"\n\U0001f525 A diferença entre o set2 e set3 são:\n{set2.difference(set3)}")#►{9, 10  }
print(f"\n\U0001f525 A diferença entre o set3 e set4 são:\n{set3.difference(set4)}")#►{11, 12, 13, 14, 15, 8}


# Questão 4️⃣3
# Faça uma função que recebe dois conjuntos e retorna os elementos únicos presentes em ambos.

def elementos_unicos(set1, set2):
    '''essa função vai comparar dois sets passado como parametros reais  e vai retornar somente os elementos unicos presentes em ambos.'''
    elementos_unicos = set1.intersection(set2)
    return elementos_unicos
set = {1, 2, 3, 4, 5, 7, 8, 9}
set0 = {2, 4, 7, 8, 9}

print(f"Os elementos em comum são:\n{elementos_unicos(set, set0)}")


# Questão 4️⃣5
# Crie um conjunto e utilize len() para verificar quantos elementos ele possui.

set00 = {1, 2, 3, 4, 5, 7, 8, 9}
print(f"\U0001f525 O conjunto possui {len(set00)} elementos.")

# Questão 4️⃣6
# Peça ao usuário para digitar 5 números e verifique quais já estão no conjunto.

set00 = {1, 2, 3, 4, 5, 7, 8, 9}
#print(f"\U0001f525 O conjunto possui {len(set00)} elementos.")

# Questão 4️⃣6
# Peça ao usuário para digitar 5 números e verifique quais já estão no conjunto.

nume = input(f"Digite cinco numeros:\n\U0001f525 ").strip().split(", ")
print("\n", nume)
num = set(nume)
for numero in set00:
    if num in set00:
        print(f"\nO número {num} já está no conjunto {set00}.")
    else:
        print(f"\nO numero {nume} não está no conjunto {set00}")

# o output não esta correto:
# Digite cinco numeros:
# 🔥 1, 2, 3, 4, 5, 6, 7, 8, 9
#  ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# O numero ['1', '2', '3', '4', '5', '6', '7', '8', '9'] não está no conjunto {1, 2, 3, 4, 5, 7, 8, 9}
# O numero ['1', '2', '3', '4', '5', '6', '7', '8', '9'] não está no conjunto {1, 2, 3, 4, 5, 7, 8, 9}
# O numero ['1', '2', '3', '4', '5', '6', '7', '8', '9'] não está no conjunto {1, 2, 3, 4, 5, 7, 8, 9}
# O numero ['1', '2', '3', '4', '5', '6', '7', '8', '9'] não está no conjunto {1, 2, 3, 4, 5, 7, 8, 9}
# O numero ['1', '2', '3', '4', '5', '6', '7', '8', '9'] não está no conjunto {1, 2, 3, 4, 5, 7, 8, 9}
# O numero ['1', '2', '3', '4', '5', '6', '7', '8', '9'] não está no conjunto {1, 2, 3, 4, 5, 7, 8, 9}
# O numero ['1', '2', '3', '4', '5', '6', '7', '8', '9'] não está no conjunto {1, 2, 3, 4, 5, 7, 8, 9}
# O numero ['1', '2', '3', '4', '5', '6', '7', '8', '9'] não está no conjunto {1, 2, 3, 4, 5, 7, 8, 9}

# Questão 4️⃣7
# Faça um algoritmo que verifica se um conjunto é igual a outro

set001 = {1, 2, 3, 4, 5, 7, 8, 9}
set002 = {1, 2, 3, 4, 5, 7, 8, 9}

if set001 == set002:
    print(f"\U0001f525 Os conjuntos são iguais.")
else:
    print(f"Os conjuntos são diferentes.")


    # Questão 4️⃣8
# Crie um sistema de cadastro de produtos onde cada item seja armazenado em um set.

produtos = set()
print(f"\U0001f525 Seus produtos são:\n{produtos}\n")
produtos = input(f"Quais produtos vc quer adicionar ao seu conjunto?Ou digite 'sair' para encerrar.\n\U0001f525 ").strip().split()
print(f"\U0001f525 Seus produtos são:\n{produtos}\n")
prod_sem_duplicats = set(produtos)
print(f"\U0001f525 Seus produtos sem duplicatas são:\n{prod_sem_duplicats}")    


# Questão 4️⃣9
# Desenvolva um programa que simule uma agenda de nomes, garantindo que não haja duplicatas.

agenda = ["Ana", "Ana", "Veronica", "Veronica", "Carla", "Carla", "Carol", "Carol", "Marcia", "Marcia", "Marcio", "Marcio", "Marcio"]
nomes_vazios = set()
for nome in agenda:
    if nome in agenda:
        print(f"\U0001f525 O nome {nome} já está na agenda.")
    else:
        print(f"\U0001f525 O nome {nome} não está na agenda.")
        nomes_vazios.add(nome)
nova_agenda = set(agenda)
print(f"\U0001f525 A nova agenda é:\n{nova_agenda}")

# Questão 5️⃣0
# Crie um sistema que registre números de CPF impedindo inserções duplicadas.

cpf = set()
cpf = input(f"Qual o número de seu cpf?\n\U0001f525 ").strip().split(", ")
print(f"\U0001f525  Seu cpf é: {cpf}")
#Output:
# Qual o número de seu cpf?
# 🔥 3...-67'
# 🔥  Seu cpf é: ['3...-67']

# Questão 5️⃣1
# Desenvolva um jogo simples que verifique se uma palavra já foi mencionada pelo usuário.



palavras = input(f"Qauis palavras vc quer adiconar ao jogo de captação de duplicatas:\n\U0001f525 ").strip().lower().split(", ")#atribuiçção a lista recem criado vindo do input().strp() que remove espaços em branco, .lower() que conerte tudo emmiusculas .split(", ") que me separa a string em sub-string em formato de lista.
print(f"As palavras que você escolheu para o joguinho de captação de duplicats foram:\n{palavras}")
joguinho = set() # conjunto vazio para armazenar as entradas do usuario
print(joguinho)

for palavr in palavras:
    if palavr in joguinho:
        print(f"\n\U0001f525 Joguinho perdeu, pois esta palavra \"{palavr}\" é única!\nEntão você ganhou meu, amigo!\n")
    else:
        print(f"\n\U0001f525 Joguinho ganhou! Pois esta palavra {palavr} é nova.\n")
        joguinho.add(palavr)

print(f"As palavras que o joguinho captou foram:\n{joguinho}\n")
palavras_duplicatas = joguinho

palavras_distintas = set(palavras)
print(f"\U0001f525 As palavras que fez vc perder o joguinho foram:\n{palavras_duplicatas}\n")

print(f"\U0001f525 As palavras que fez vc ganhar o joguinho foram:\n{palavras_distintas.difference(palavras_duplicatas)}\n")

print(f"\U0001f525 Quais foram as palavras que vc escolheu que te levaram ao impasse da temporaria derrota:\n{palavras_distintas.intersection(palavras_duplicatas)}\n")

print(f"\U0001f525 As palavras que vc escolheu e o joguinho também são:\n{palavras_distintas.symmetric_difference(palavras_duplicatas)}\n")


# Questão 5️⃣2
# Simule um sistema de votação que permita a cada pessoa votar apenas uma vez.

while True:
    try:
        cand = set()
        cand2 = set()
        usuario = input(f"Em quem vc quer votar? Se for no cand digite '1', se for na cand2 digite '2' ou 'sair' para encerrar")

        if usuario == 'sair':
            print(f"\U0001f44b Você optou por finalizara votação")
            break

        elif not in usuario:
            raise ValueError(f"\n\U0000274c Digite em quem vc quer votar ('1' para cand e '2' para cand2, ou 'sair para encerrar)")
        
        opções = int(usuario)

        if not opções.isdigit():
            raise TypeError(f"\n\U0000274c Você digitou a informação errada. ('1' para cand e '2' para cand2, ou 'sair para encerrar)")

        elif usuario == 1:
            for 


# Questão 5️⃣3
# Crie um programa que compare duas listas e exiba apenas os elementos em comum.

lista = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

lista_comum = set(lista).intersection(set(lista2))
print(lista_comum)

# dados = set()
# dados = set(input(f"Adicione 5 elementos separados por virgula\n").strip().lower().split(", "))
# print(f" Os elementos que estão na variavel dados são: {dados}")
# # abaixo o output:
# # Adicione 5 elementos separados por virgula
# # 1, 2, 3, 4, 5
# #  Os elementos que estão na variavel dados são: ['1', '2', '3', '4', '5']
# # PS C:\Users\Pichau\OneDrive\Área de Trabalho\estudo_conjuntos> & C:/Users/Pichau/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Pichau/OneDrive/Área de Trabalho/estudo_conjuntos/conjuntos.py"
# # Adicione 5 elementos separados por virgula
# # 1, 2, 32, 5, 32, 2, 2, 4, 5, 1
# #  Os elementos que estão na variavel dados são: {'4', '5', '1', '2', '32'}
# # PS C:\Users\Pichau\OneDrive\Área de Trabalho\estudo_conjuntos>

# *************************************************************
def visualizar_conjunto(lista):
    '''Essa função tem por objetivo visualizar o elementos.'''

    print(f"\nOs elementos que vc inseriu são:\n{lista}")
def visualizar_sem_duplicats(lista):
    '''Essa função recebe uma lista e a converte em set para remoção de duplicatas. '''
    sem_duplicatas = list(set(lista))
    sem_duplicatas.sort()
    print(f"Agora sua lista esta sem duplicatas:\n{sem_duplicatas}")
    return sem_duplicatas
def inserção_de_dados(lista):
    '''Essa função vai ser de incremento a lista.'''
    novos_dados = input(f"\nQuais elementos vc quer inserir? (separados por vírgula)\n").strip().lower().split(", ")
    lista.extend(novos_dados)
    
    print(f"\nA lista está assim atualmente:\n{lista}")
    return lista.sort()
# Questão 3️⃣0
# Faça um programa que converta uma lista com números repetidos em um conjunto, eliminando duplicatas.
def programinha_sem_duplicatas():
    '''aqui eu crio uma função que vai gerar um loop  para que o usuario tenha ciencia de que enquanto ele não confirmar com sair, o loop de inserção vai continuar e adicionr elementos, mas a convesão em set() vai eliminar todas duplicatas. '''
    lista = []
    while True:
        try:
            print("\n🔥 Escolha uma opção abaixo:")
            print("0) Inserir elementos.")
            print("1) Visualizar todas as inserções.")
            print("2) Visualizar lista sem duplicatas.")
            print("3) Encerrar operação.")

            dados = input(f"Digite a opção desejada:\n\U0001f525 ").strip()
                       
            if not dados:
                raise ValueError(f"\U000026a0 Você não digitou nada.")

            elif not dados.isdigit():
                raise ValueError(f"\U000026a0 Digite apenas os números descritos na opção da mensagem principal")
            
            dados = int(dados)

            if dados < 0 and dados > 3:
                raise ValueError(f"\U0000274c Opção inválida. Escolha as opções descritas na mensagem principal.")
        
            elif dados == 3:
                print(f"\n\U0001f44b Até mais.")
                break

            elif dados == 0:
                inserção_de_dados(lista)

            elif dados == 1:
                visualizar_conjunto(lista)

            elif dados == 2:
                visualizar_sem_duplicats(lista)
            
            else:
                raise ValueError(f"|U000026a0 Digite um aopção entre 0 e 3")

        except ValueError as v:
            print(f"\U0000274c Erro: {v}")
        else:
            print(f"A operação funcionou.")
        finally:
            print(f"\U0001f44b Encerrando operação...")
#programinha_sem_duplicatas()

#palavras = input(f"Digite 10 palavras:\n\U0001f525 ").strip().lower().split(", ")
#print(f"{set(palavras)}")
# #PS C:\Users\Pichau\OneDrive\Área de Trabalho\estudo_conjuntos> & C:/Users/Pichau/AppData/Local/Programs/Python/Python313/python.exe "c:/Users/Pichau/OneDrive/Área de Trabalho/estudo_conjuntos/conjuntos.py"
# Digite 10 palavras:
# 🔥  café, café, pão, pão, chá, chá, leite, leite, bolacha, bolacha, café, café, pão, pão, chá, chá, leite, leite, bolacha, bolacha
# {'café', 'chá', 'pão', 'leite', 'bolacha'}
# PS C:\Users\Pichau\OneDrive\Área de Trabalho\estudo_conjuntos> 


set00 = {1, 2, 3, 4, 5, 7, 8, 9}
#print(f"\U0001f525 O conjunto possui {len(set00)} elementos.")

# Questão 4️⃣6
# Peça ao usuário para digitar 5 números e verifique quais já estão no conjunto.

# nume = input(f"Digite cinco numeros:\n\U0001f525 ").strip().split(", ")
# print("\n", nume)
# num = set(nume)
# for numero in set00:
#     if num in set00:
#         print(f"\nO número {num} já está no conjunto {set00}.")
#     else:
#         print(f"\nO numero {nume} não está no conjunto {set00}")

# Questão 4️⃣8
# Crie um sistema de cadastro de produtos onde cada item seja armazenado em um set.

# def sistema(): 
#     '''aqui eu vou criar um sistema de cadastramento de produtos.'''
   
        
#     while True:
#         try:
#             produtos = set()
#             print(f"\U0001f525 Seus produtos são:\n{produtos}")
#             produtos = input(f"Quais produtos vc quer adicionar ao seu conjunto?Ou digite 'sair' para encerrar.").strip().split()


            



#         except:
#         else:
#             print(f"\n\U0001f525")           
#         finally:
#             print(f"\U0001f44b Encerrando operação...")     

# produtos = set()
# print(f"\U0001f525 Seus produtos são:\n{produtos}\n")
# produtos = input(f"Quais produtos vc quer adicionar ao seu conjunto?Ou digite 'sair' para encerrar.\n\U0001f525 ").strip().split()
# print(f"\U0001f525 Seus produtos são:\n{produtos}\n")
# prod_sem_duplicats = set(produtos)
# print(f"\U0001f525 Seus produtos sem duplicatas são:\n{prod_sem_duplicats}")    

# agenda = ["Ana", "Ana", "Veronica", "Veronica", "Carla", "Carla", "Carol", "Carol", "Marcia", "Marcia", "Marcio", "Marcio", "Marcio"]
# nomes_vistos = set()  # Criamos um conjunto para armazenar os nomes que já apareceram

# for nome in agenda:# eu não entendi a lógica: para cada nome em agenda faça:
#     if nome in nomes_vistos:  # Se o nome já estiver no conjunto, significa que já apareceu antes  ► se nome esta em nomes_vistos faça, se não adicione ao set, ate aqui beleza, mas na condição do if nomes_vistos esta vazio, então como ele pode verificar no set quando os nomes que estão sendo verificados estão na agenda que é uma lista?

#     # então a verificação é feita elemento a elemnto dentro de set, mas em existencia de elemento, não em posição de iteração?
#         print(f"🔥 O nome {nome} já estava na agenda.")
#     else:# equando foi que houve as remoções de duplicatas, fopi na iteração dentro da lista agenda feita pelo for, de forma meio implicita??subjetiva...assim, a cada iteração, se já estiver na ageda, o if entra em cena e so imprime que esta na agenda, mas se não estiver na agenda, averiguação que é feita em cada iteração, eé adicionado ao set nomes_vazios
#         print(f"🔥 O nome {nome} é novo na agenda.")
#         nomes_vistos.add(nome)  # Adicionamos o nome ao conjunto para futuras verificações
# # não vejo correlação entre o set nomes_vistos e agendas
# nova_agenda = set(agenda)  # Remove duplicatas convertendo para um conjunto
# print(f"\n🔥 A nova agenda sem duplicatas é:\n{nova_agenda}")

# # mas como a nova agenda recebe o no_set que contem nomes unicos se não é feita atribuição explicita?

# Questão 5️⃣1
# Desenvolva um jogo simples que verifique se uma palavra já foi mencionada pelo usuário.


# palavras = input(f"Qauis palavras vc quer adiconar ao jogo de captação de duplicatas:\n\U0001f525 ").strip().lower().split(", ")#atribuiçção a lista recem criado vindo do input().strp() que remove espaços em branco, .lower() que conerte tudo emmiusculas .split(", ") que me separa a string em sub-string em formato de lista.
# print(f"As palavras que você escolheu para o joguinho de captação de duplicats foram:\n{palavras}")
# joguinho = set() # conjunto vazio para armazenar as entradas do usuario
# print(joguinho)

# for palavr in palavras:
#     if palavr in joguinho:
#         print(f"\n\U0001f525 Joguinho perdeu, pois esta palavra \"{palavr}\" é única!\nEntão você ganhou meu, amigo!\n")
#     else:
#         print(f"\n\U0001f525 Joguinho ganhou! Pois esta palavra {palavr} é nova.\n")
#         joguinho.add(palavr)

# print(f"As palavras que o joguinho captou foram:\n{joguinho}\n")
# palavras_duplicatas = joguinho

# palavras_distintas = set(palavras)
# print(f"\U0001f525 As palavras que fez vc perder o joguinho foram:\n{palavras_duplicatas}\n")

# print(f"\U0001f525 As palavras que fez vc ganhar o joguinho foram:\n{palavras_distintas.difference(palavras_duplicatas)}\n")

# print(f"\U0001f525 Quais foram as palavras que vc escolheu que te levaram ao impasse da temporaria derrota:\n{palavras_distintas.intersection(palavras_duplicatas)}\n")

# print(f"\U0001f525 As palavras que vc escolheu e o joguinho também são:\n{palavras_distintas.symmetric_difference(palavras_duplicatas)}\n")

# print(f"\U0001f525 As palavras que fez vc ganhar o joguinho foram:\n{palavras_vencedora.difference(palavras_duplicatas)}")

# print(f"\U0001f525 As palavras que fez vc ganhar o joguinho foram:\n{palavras_vencedora.difference(palavras_duplicatas)}")


