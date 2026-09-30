from personagem import Personagem


class Guerreiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=120,
            ataque=20,
            defesa=15
        )

    def atacar(self, inimigo):
        dano = self.ataque - inimigo.defesa
        if dano > 0:
            inimigo.vida -= dano
            print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")
        else:
            print(f"{self.nome} atacou {inimigo.nome}, mas não causou dano.")
       