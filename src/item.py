class Item:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def usar(self, personagem):
        # TODO: implementar efeito do item
        pass
class Potion(Item):

    def __init__(self, nome, valor, quantidade):
        super().__init__(nome, valor)
        self.quantidade = quantidade

    def usar(self, personagem):
        if self.quantidade > 0:
            personagem.vida += 20  #  aumenta a vida do personagem
            self.quantidade -= 1
            print(f"{personagem.nome} usou {self.nome} e recuperou 20 de vida!")
        else:
            print(f"{self.nome} não tem mais quantidade disponível.")