import random

user_wins = 0
pc_wins = 0
#             0        1         2
options = ["pedra", "papel", "tesoura"]

while True:
    user_input = input("Digite pedra, papel, tesoura ou S para sair. ").lower()
    if user_input == "s":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    pc_escolhe = options[random_number]
    print("Computador escolheu", pc_escolhe + ".")

    if user_input == "pedra" and pc_escolhe == "tesoura":
        print("Você venceu essa! Mas não por muito tempo \U0001F600")
        user_wins += 1
    elif user_input == "tesoura" and pc_escolhe == "papel":
        print("Você venceu!")
        user_wins += 1
    elif user_input == "papel" and pc_escolhe == "pedra":
        print("Você venceu! MELECA!")
        user_wins += 1

    else:
        print("Você perdeu, otário hehehehe")