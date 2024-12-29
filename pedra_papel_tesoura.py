import random

pedra = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papel = """    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
tesoura = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!\n")
jogador = int(
    input("""[1] Pedra
[2] Papel
[3] Tesoura

Escolha uma jogada: """))

computador = random.randint(1, 3)

if jogador == 1:
    print(pedra)
    print("Você escolheu Pedra")
elif jogador == 2:
    print(papel)
    print("Você escolheu Papel")
elif jogador == 3:
    print(tesoura)
    print("Você escolheu Tesoura")

if computador == 1:
    print(pedra)
    print("O computador escolheu Pedra")
elif computador == 2:
    print(papel)
    print("O computador escolheu Papel")
elif computador == 3:
    print(tesoura)
    print("O computador escolheu Tesoura")

if jogador == 1 and computador == 3:
    print("\nVocê ganhou!")
elif jogador == 2 and computador == 1:
    print("\nVocê ganhou!")
elif jogador == 3 and computador == 2:
    print("\nVocê ganhou!")
elif jogador == computador:
    print("\nEmpatou!")
else:
    print("\nVocê perdeu!")
