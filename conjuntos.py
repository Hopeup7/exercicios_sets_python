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
