from mago import Gelo, Raio, Fogo, Mago


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
            print("4 - Usar magia (apenas para magos)")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
              self.jogador.atacar(self.inimigo)
                

            elif opcao == "2":
                
                pass

            elif opcao == "3":
                print("Você fugiu da batalha!")
                return
            elif opcao == "4":
                if isinstance(self.jogador, Mago):
                    print("Escolha a magia:")
                    print("1 - Fogo")
                    print("2 - Gelo")
                    print("3 - Raio")
                    escolha_magia = input("Digite o número da magia: ")

                    if escolha_magia == "1":
                        magia = Fogo()
                    elif escolha_magia == "2":
                        magia = Gelo()
                    elif escolha_magia == "3":
                        magia = Raio()
                    else:
                        print("Opção inválida.")
                        continue

                    self.jogador.usar_magia(magia, self.inimigo)
                else:
                    print("Apenas magos podem usar magias.")
            else:
                print("Opção inválida.")
                continue

            if self.inimigo.esta_vivo():
                self.inimigo.atacar(self.jogador)
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
                        pass

                    elif opcao == "3":
                        print("Você fugiu da batalha!")
                        return

                    else:
                        print("Opção inválida.")
                        continue

                    if self.inimigo.esta_vivo():
                        self.inimigo.atacar(self.jogador)
        if self.jogador.esta_vivo():
            print("\nParabéns! Você venceu a batalha!")
        else:
            print("\nVocê foi derrotado na batalha.")
