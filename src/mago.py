from personagem import Personagem

class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=80,
            ataque=30,
            defesa=5,
            
        )

        self.mana = 100

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa
        if dano > 0:
            alvo.receber_dano(dano)
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        else:
            print(f"{self.nome} atacou {alvo.nome}, mas não causou dano.")

    def usar_magia(self, magia, alvo):
            if self.mana >= magia.custo:
                self.mana -= magia.custo
                dano = magia.dano - alvo.defesa
                if dano > 0:
                    alvo.receber_dano(magia.dano)
                    print(f"{self.nome} usou magia em {alvo.nome} causando {dano} de dano!")
                else:
                    print(f"{self.nome} usou magia em {alvo.nome}, mas não causou dano.")
            else:
                print("O mago não possui mana suficiente.")
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
    
