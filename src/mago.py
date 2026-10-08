from src.personagem import Personagem


class Mago(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=80,
            ataque=30,
            defesa=5
        )

        self.mana = 100

    def atacar(self, alvo):
        if alvo is None:
            raise ValueError("É necessário informar um alvo.")

        alvo.receber_dano(self.ataque)
        return alvo.vida

    def usar_magia(self, alvo):
        if self.mana < 10:
            print("O mago não possui mana suficiente.")
            return False

        if alvo is None:
            raise ValueError("É necessário informar um alvo.")

        self.mana -= 10
        alvo.receber_dano(self.ataque + 10)
        return True
