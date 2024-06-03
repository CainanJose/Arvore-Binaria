class Aniversariante:  # Definição da classe Aniversariante
    def __init__(self, nome, dia, mes):
        self.nome = nome
        self.dia = dia
        self.mes = mes

    def __str__(self):
        return f"{self.nome} - {self.dia}/{self.mes}"