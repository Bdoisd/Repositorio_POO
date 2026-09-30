class Item:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def usar(self, personagem):
        # TODO: implementar efeito do item
        pass
class Poção_Mana(Item):
    def __init__(self):
        super().__init__(nome="Poção de Mana", valor=30)

    def usar(self, personagem):
        if hasattr(personagem, 'mana'):
            personagem.mana += 30
            print(f"{personagem.nome} usou {self.nome} e recuperou 30 de mana!")
        else:
            print(f"{personagem.nome} não pode usar {self.nome}.")