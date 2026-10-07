from guerreiro import Guerreiro
from inimigo import Inimigo
from batalha import Batalha
from mago import Mago
 
def main():
    print("Bem-vindo ao jogo")
    print("Escolha seu personagem:")
    print("1 - Guerreiro")
    print("2 - Mago")
    escolha = input("Digite o número do personagem: ")

    if escolha == "1":
        jogador = Guerreiro("Arthur")
    elif escolha == "2":
        jogador = Mago("Merlin")
    else:
        print("Opção inválida.")
        return
    inimigos=[Inimigo("Goblin", 50, 22, 5), Inimigo("Orc", 80, 25, 20), Inimigo("Mago Inimigo", 60, 20, 10), Inimigo("Boss Final", 150, 30, 15)]
    for inimigo in inimigos:
        print(f"\nUma batalha começou contra {inimigo.nome}!")
        batalha = Batalha(jogador, inimigo)
        batalha.iniciar()
        if not jogador.esta_vivo():
            print("Você foi derrotado!")
            break
        print(f"voce foi derrotado pelo {inimigo.nome} e perdeu a batalha")
        else:
        print(f"Você derrotou {inimigo.nome} e venceu a batalha!")

    

    


if __name__ == "__main__":
    main()
