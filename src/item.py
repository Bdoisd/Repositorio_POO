class Item:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def usar(self, personagem):
        return False


class Potion(Item):

    def __init__(self, nome="Poção", valor=10, quantidade=1):
        super().__init__(nome, valor)
        self.quantidade = quantidade

    def usar(self, personagem):
        if self.quantidade <= 0:
            return False

        self.quantidade -= 1
        if hasattr(personagem, "vida"):
            personagem.vida = min(personagem.vida + self.valor, 100)
        return True


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
        if item not in self.itens:
            print("Item não encontrado no inventário.")
            return False

        if hasattr(item, "quantidade") and item.quantidade <= 0:
            self.remover_item(item)
            return False

        if item.usar(personagem):
            if hasattr(item, "quantidade") and item.quantidade == 0:
                self.remover_item(item)
            return True

        return False

    def mostrar_inventario(self):
        if not self.itens:
            print("O inventário está vazio.")
            return

        print("Itens no inventário:")
        for item in self.itens:
            print(f"- {item.nome} (Valor: {item.valor})")