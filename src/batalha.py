class Batalha:

    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo

    def iniciar(self):

        print("=" * 40)
        print("        INÍCIO DA BATALHA")
        print("=" * 40)

        while self.jogador.esta_vivo() and self.inimigo.esta_vivo():

            print("\n--- STATUS ---")
            self.jogador.mostrar_status()
            self.inimigo.mostrar_status()

            print("\n--- AÇÕES ---")
            print("1 - Atacar")
            print("2 - Usar item")
            print("3 - Fugir")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.jogador.atacar(self.inimigo)
            elif opcao == "2":
                if hasattr(self.jogador, "inventario"):
                    item = self.jogador.inventario.itens[0] if self.jogador.inventario.itens else None
                    if item is not None:
                        self.jogador.inventario.usar_item(item, self.jogador)
                    else:
                        print("Seu inventário está vazio.")
                else:
                    print("Você não possui inventário.")
            elif opcao == "3":
                print("Você fugiu da batalha!")
                return
            else:
                print("Opção inválida.")
                continue

            if not self.inimigo.esta_vivo():
                break

            self.inimigo.atacar(self.jogador)

        if self.jogador.esta_vivo():
            print(f"{self.jogador.nome} venceu a batalha!")
        else:
            print(f"{self.inimigo.nome} venceu a batalha!")
