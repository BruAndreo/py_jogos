import random
import utils.util as utils

numero_min = 1
numero_max = 100
pontuacao = 1000

def definir_numero_tentativas():
    nivel = utils.selecionar_dificuldade()

    if nivel == 1:
        return 10
    elif nivel == 2:
        return 5
    elif nivel == 3: 
        return 3

def numero_fora_intervalo(num):
    if ((num < numero_min) or (num > numero_max)):
        print(f"Você deve digitar um numero entre {numero_min} e {numero_max}")
        return True
    return False

def diminuir_pontuacao(pontos_perdidos):
    pontuacao = pontuacao - pontos_perdidos

def jogar():
    utils.boas_vindas_msg("Bem vindo ao jogo de Adivinhação")

    total_tentativas = definir_numero_tentativas()
    secret_number = random.randrange(numero_min, numero_max + 1)

    for tentativa_atual in range(1, total_tentativas + 1):
        print("> Tentativa {}/{}".format(tentativa_atual, total_tentativas))

        chute = int(input(">> Digite um numero entre {} e {}: ".format(numero_min, numero_max)))

        if numero_fora_intervalo(chute):
            continue

        acertou = secret_number == chute

        if acertou:
            print("Acertou miseravi")
            break
        elif (secret_number < chute):
            print("Erroouu - É pra baixo")
            diminuir_pontuacao(chute - secret_number)
        else:
            print("Erroouu - É pra cima")
            diminuir_pontuacao(secret_number - chute)

    if not acertou:
        diminuir_pontuacao(pontuacao)

    print(f"Fim do jogo - O numero correto é: {secret_number}")
    print(f"Sua pontuação foi: {pontuacao}")

if (__name__ == "__main__"):
    jogar()