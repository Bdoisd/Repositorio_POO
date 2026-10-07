from personagem import Personagem


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque,
            defesa=defesa
        )

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa
        if dano > 0:
            alvo.vida -= dano
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        else:
            print(f"{self.nome} atacou {alvo.nome}, mas não causou dano.")
class Goblin(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Goblin",
            vida=50,
            ataque=15,
            defesa=5
        )
class Orc(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Orc",
            vida=80,
            ataque=25,
            defesa=20
        )
class MagoInimigo(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Mago Inimigo",
            vida=60,
            ataque=20,
            defesa=10
        )
class Bossfinal(Inimigo):
    def __init__(self):
        super().__init__(
            nome="Boss Final",
            vida=150,
            ataque=30,
            defesa=15
        )