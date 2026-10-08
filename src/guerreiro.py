from src.personagem import Personagem


class Guerreiro(Personagem):

    def __init__(self, nome):
        super().__init__(
            nome=nome,
            vida=120,
            ataque=20,
            defesa=15
        )

    def atacar(self, alvo):
        if alvo is None:
            raise ValueError("É necessário informar um alvo.")

        alvo.receber_dano(self.ataque)
        return alvo.vida
