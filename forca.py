import utils.util as utils

def jogar():
    utils.boas_vindas_msg("Olá seja bem-vindo ao jogo de forca")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for l in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 6

    print(letras_acertadas)
    
    while (not enforcou and not acertou):
        print(f"Você tem {erros} tentativas")
        chute = input("Qual letra? ").strip().upper()

        if chute not in palavra_secreta:
            erros -= 1
            continue
        
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    print("Fim de jogo")

    if acertou:
        print("Parabéns! Você Ganhou!")

if (__name__ == "__main__"):
    jogar()