import random


def jogar():

    boas_vindas = "Olá seja bem-vindo ao jogo de adivinhação"
    asteriscos = len(boas_vindas) * '*'

    print(asteriscos)
    print(boas_vindas)
    print(asteriscos)

    numero_min = 1
    numero_max = 100
    total_tentativas = 0
    pontuacao = 1000
    secret_number = random.randrange(numero_min, numero_max + 1)

    print("Selecione o nível de dificuldade do jogo")
    print("1 - Fácil (10 tentativas)")
    print("2 - Médio (5 tentativas)")
    print("3 - Dificil (3 tentativas)")

    nivel = int(input("Nível de Dificuldade: "))

    if nivel == 1:
        total_tentativas = 10
    elif nivel == 2:
        total_tentativas = 5
    elif nivel == 3: 
        total_tentativas = 3
    else:
        print("É necessário informar um nível de dificuldade válido")
        exit()


    for tentativa_atual in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa_atual, total_tentativas))

        chute = int(input("Digite seu numero entre {} e {}: ".format(numero_min, numero_max)))

        if ((chute < numero_min) or (chute > numero_max)):
            print(f"Você deve digitar um numero entre {numero_min} e {numero_max}")
            continue

        acertou = secret_number == chute

        if acertou:
            print("Acertou miseravi")
            break
        elif (secret_number < chute):
            print("Erroouu - É pra baixo")
            pontuacao = pontuacao - (chute - secret_number)
        else:
            print("Erroouu - É pra cima")
            pontuacao = pontuacao - (secret_number - chute)

    if not acertou:
        pontuacao = 0

    print(f"Fim do jogo - O numero correto é: {secret_number}")
    print(f"Sua pontuação foi: {pontuacao}")

if (__name__ == "__main__"):
    jogar()