from src.guerreiro import Guerreiro


def test_guerreiro_esta_vivo():

    guerreiro = Guerreiro("Arthur")

    assert guerreiro.esta_vivo() is True


def test_personagem_recebe_dano():
    personagem = Guerreiro("Arthur", vida=100, ataque=20, defesa=10)
    personagem.receber_dano(15)
    assert personagem.vida == 85


def test_personagem_morre():
    personagem = Guerreiro("Arthur", vida=100, ataque=20, defesa=10)
    personagem.receber_dano(100)
    assert personagem.vida == 0

def test_personagem_nao_morre_com_defesa():
    personagem = Guerreiro("Arthur", vida=100, ataque=20, defesa=10)
    personagem.receber_dano(5)
    assert personagem.vida == 100
def test_guerreiro_ataca():
    # TODO
    pass
