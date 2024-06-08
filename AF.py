
from Aniversariante import Aniversariante
from BinaryTree import BinaryTree

class GerenciadorAniversarios:
    def __init__(self):
        self.arvore = BinaryTree()
    

    def inserirAniversariante(self, aniversariante):
        mes = aniversariante.mes
        if not self.arvore.search(mes):
            self.arvore.insert(mes)

        mes = self.buscaMes(self.arvore.root, mes)
        mes.aniversariantes.append(aniversariante)

    def buscaMes(self, no, mes):
        if no is None:
            return None
        if no.key == mes:
            return no
        elif mes < no.key:
            return self.buscaMes(no.left, mes)
        else:
            return self.buscaMes(no.right, mes)

    def aniversarianteMes(self, mes, dia=None):
        mes = self.buscaMes(self.arvore.root, mes)
        if mes:
            if dia is None:
                return mes.aniversariantes  # Retorna a lista completa do mês
            else:
                aniver = []
                atual = mes.aniversariantes.head
                while atual:
                    if atual.value.dia == dia:
                        aniver.append(atual.value)
                    atual = atual.next
                return aniver
        else:
            return None

    def menu(self):
        atual = 2024
        while True:
            print("\n")
            print("\nMenu:")
            print("1. Inserir um Aniversariante")
            print("2. Buscar Aniversariantes por Mês")
            print("3. Inserir Vários Aniversariantes")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                while True:
                    try:
                        nome = input("Nome: ")
                        if not nome:  # Verifica se o nome não está vazio
                            raise ValueError("O nome não pode ser vazio.")
                    except ValueError as e:
                        print("Entrada inválida. Por favor insira um nome válido.")
                        continue
                    
                    while True: 
                        try:
                            dia = int(input("Dia: "))
                            if dia < 1 or dia > 31: #Verifica se o dia e valido
                                raise ValueError("O dia deve estar entre 1 e 31.")
                            break
                        except ValueError as e:
                            print(f"Entrada inválida. {e}")
                            
                    while True:
                        try: 
                            mes = int(input("Mês: "))
                            if mes < 1 or mes > 12:
                                raise ValueError("Mês inválido. O mês deve estar entre 1 e 12.")
                            break
                        except ValueError:
                            print("Mês inválido. O mês deve estar entre 1 e 12.")
                        
                    while True:
                        try:
                            ano = int(input("Ano: "))
                            if ano < 1:  # Verifica se o ano é positivo
                                raise ValueError("O ano deve ser um número positivo.")
                            break
                        except ValueError as e:
                            print(f"Entrada inválida. {e}")

                    self.inserirAniversariante(Aniversariante(nome, dia, mes, ano))
                    print(f"Usuário {nome} que faz aniversário no dia {dia}/{mes}/{ano} cadastrado com sucesso!")
                    break
                gerenciador.menu()

            elif opcao == '2':  # Submenu de busca
                while True:
                    print("\nBuscar Aniversariantes:")
                    print("1. Listar todos os Aniversariantes do Mês")
                    print("2. Buscar Aniversariante por Mês e Dia")
                    print("3. Voltar ao Menu Principal")
                    subopcao = input("Escolha uma opção: ")
                
                    if subopcao == '1':
                        try:
                            mes = int(input("Mês: "))
                            listaAniver = self.aniversarianteMes(mes)
                            if listaAniver:
                                print(f"\nAniversariantes do mês {mes}:")
                                listaAniver.display()
                            else:
                                print(f"\nNenhum aniversariante encontrado para o mês {mes}.")
                        except ValueError:
                            print("Entrada inválida. Por favor insira um número inteiro para o mês correspondente.")
                            
                    elif subopcao == '2':
                        try:
                            mes = int(input("Mês: "))
                            dia = int(input("Dia: "))
                            listaAniver = self.aniversarianteMes(mes, dia)
                            if listaAniver:
                                print(f"\nAniversariantes do dia {dia}/{mes}:")
                                for aniversariante in listaAniver:
                                    print(aniversariante)
                            else:
                                print(f"\nNenhum aniversariante encontrado para o dia {dia}/{mes}.")
                        except ValueError:
                            print("Entrada inválida. Digite um valor válido para o dia e o mês.")
                            
                    elif subopcao == '3':
                        break
                    else:
                        print("Opção inválida!")

            elif opcao == '3':
                qtd = int(input("Quantos aniversariantes deseja inserir? "))
                for i in range(qtd):
                    try: 
                        nome = input(f"Nome do aniversariante {i+1}: ")
                        dia = int(input(f"Dia do aniversário de {nome}: "))
                        mes = int(input(f"Mês do aniversário de {nome}: "))
                        ano = int(input(f"Ano do aniversário de {nome}: "))
                        self.inserirAniversariante(Aniversariante(nome, dia, mes, ano))
                    except ValueError:
                        print("Entrada inválida. Digite um valor válido para o dia, mês e ano")
            elif opcao == '4':
                break
            else:
                print("Opção inválida!")


# Criação de aniversariantes e inserção na árvore
gerenciador = GerenciadorAniversarios()
aniversariantes_predefinidos = [
    Aniversariante("João", 4, 6, 2001,),
    Aniversariante("Maria", 22, 3, 2004),
    Aniversariante("Pedro", 8, 5, 2001),
    Aniversariante("Ana", 10, 12, 2000),
]

for aniversariante in aniversariantes_predefinidos:
    gerenciador.inserirAniversariante(aniversariante)

gerenciador.menu()

