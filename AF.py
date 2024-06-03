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
                aniversariantes_encontrados = []
                atual = mes.aniversariantes.head
                while atual:
                    if atual.value.dia == dia:
                        aniversariantes_encontrados.append(atual.value)
                    atual = atual.next
                return aniversariantes_encontrados
        else:
            return None

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Inserir um Aniversariante")
            print("2. Buscar Aniversariantes por Mês")
            print("3. Inserir Vários Aniversariantes")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Nome: ")
                dia = int(input("Dia: "))
                mes = int(input("Mês: "))
                self.inserirAniversariante(Aniversariante(nome, dia, mes))
            elif opcao == '2':  # Submenu de busca
                while True:
                    print("\nBuscar Aniversariantes:")
                    print("1. Listar todos os Aniversariantes do Mês")
                    print("2. Buscar Aniversariante por Mês e Dia")
                    print("3. Voltar ao Menu Principal")

                    subopcao = input("Escolha uma opção: ")

                    if subopcao == '1':
                        mes = int(input("Mês: "))
                        listaAniver = self.aniversarianteMes(mes)
                        if listaAniver:
                            print(f"\nAniversariantes do mês {mes}:")
                            listaAniver.display()
                        else:
                            print(f"\nNenhum aniversariante encontrado para o mês {mes}.")
                    elif subopcao == '2':
                        mes = int(input("Mês: "))
                        dia = int(input("Dia: "))
                        listaAniver = self.aniversarianteMes(mes, dia)
                        if listaAniver:
                            print(f"\nAniversariantes do dia {dia}/{mes}:")
                            for aniversariante in listaAniver:
                                print(aniversariante)
                        else:
                            print(f"\nNenhum aniversariante encontrado para o dia {dia}/{mes}.")
                    elif subopcao == '3':
                        break
                    else:
                        print("Opção inválida!")

            elif opcao == '3':
                qtd = int(input("Quantos aniversariantes deseja inserir? "))
                for i in range(qtd):
                    nome = input(f"Nome do aniversariante {i+1}: ")
                    dia = int(input(f"Dia do aniversário de {nome}: "))
                    mes = int(input(f"Mês do aniversário de {nome}: "))
                    self.inserirAniversariante(Aniversariante(nome, dia, mes))

            elif opcao == '4':
                break
            else:
                print("Opção inválida!")


# Criação de aniversariantes e inserção na árvore
gerenciador = GerenciadorAniversarios()
aniversariantes_predefinidos = [
    Aniversariante("João", 15, 5),
    Aniversariante("Maria", 22, 3),
    Aniversariante("Pedro", 8, 5),
    Aniversariante("Ana", 10, 1),
]

for aniversariante in aniversariantes_predefinidos:
    gerenciador.inserirAniversariante(aniversariante)

gerenciador.menu()

