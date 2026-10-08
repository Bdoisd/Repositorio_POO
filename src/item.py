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

    def usar_item(self, item, personagem):
        if item in self.itens:
        item.usar(personagem)

    if hasattr(item, "quantidade") and item.quantidade <= 0:
       self.remover_item(item)
    else:
     print("Item não encontrado no inventário.")