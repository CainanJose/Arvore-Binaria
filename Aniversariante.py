from datetime import datetime

class Aniversariante:
    def __init__(self, nome, dia, mes, ano):
        self.nome = nome
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def idade(self):
        nasc = datetime(self.ano, self.mes, self.dia)
        diaAtual = datetime.now()
        idade = diaAtual.year - nasc.year

        if (diaAtual.month, diaAtual.day) < (nasc.month, nasc.day): 
            idade -= 1  
        return idade

    def __str__(self):
        return f"{self.nome} - {self.dia}/{self.mes}/{self.ano} - Idade: {self.idade()} anos"