from item import Poção_Mana
from personagem import Personagem

class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=80,
            ataque=30,
            defesa=5,
            Poder_magico=70,
        )

        self.mana = 100

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa
        if dano > 0:
            alvo.vida -= dano
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        else:
            print(f"{self.nome} atacou {alvo.nome}, mas não causou dano.")

    def usar_magia(self, magia, alvo):
            if self.mana >= magia.custo:
                self.mana -= magia.custo
                dano = magia.dano - alvo.defesa
                if dano > 0:
                    alvo.vida -= dano
                    print(f"{self.nome} usou magia em {alvo.nome} causando {dano} de dano!")
                else:
                    print(f"{self.nome} usou magia em {alvo.nome}, mas não causou dano.")
            else:
                print("O mago não possui mana suficiente.")
class Inventario:
    def __init__(self):
        self.itens = [Poção_Mana()]  # Inicializa com 4 poções

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
class Magia:
    def __init__(self, nome, dano, custo):
        self.nome = nome
        self.dano = dano
        self.custo = custo
class Fogo(Magia):
    def __init__(self):
        super().__init__(nome="Fogo", dano=30, custo=20)
class Gelo(Magia):
    def __init__(self):
        super().__init__(nome="Gelo", dano=20, custo=15)
class Raio(Magia):
    def __init__(self): 
        super().__init__(nome="Raio", dano=40, custo=25)
    
