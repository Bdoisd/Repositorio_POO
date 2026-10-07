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
class Potion(Item):

    def __init__(self, nome, valor, quantidade):
        super().__init__(nome, valor)
        self.quantidade = quantidade

    def usar(self, personagem):
        if self.quantidade > 0:
            personagem.vida = min(personagem.vida_maxima, personagem.vida + 20)  #  aumenta a vida do personagem
            self.quantidade -= 1
            print(f"{personagem.nome} usou {self.nome} e recuperou 20 de vida!")
        else:
            print(f"{self.nome} não tem mais quantidade disponível.")
class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
        else:
            print("Item não encontrado no inventário.")

    def usar_item(self, item, personagem):
        if item in self.itens:
            item.usar(personagem)
            self.remover_item(item)
        else:
            print("Item não encontrado no inventário.")

    def mostrar_inventario(self):
        if not self.itens:
            print("O inventário está vazio.")
        else:
            print("Itens no inventário:")
            for item in self.itens:
                print(f"- {item.nome} (Valor: {item.valor})")