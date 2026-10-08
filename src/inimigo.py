from src.personagem import Personagem


class Inimigo(Personagem):

    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(
            nome=nome,
            vida=vida,
            ataque=ataque,
            defesa=defesa
        )

    def atacar(self, alvo):
        if alvo is None:
            raise ValueError("É necessário informar um alvo.")

        alvo.receber_dano(self.ataque)
        return alvo.vida
