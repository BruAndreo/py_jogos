import random
import utils.util as utils
import utils.mensagens as mensagens

def jogar():
    utils.boas_vindas_msg("Olá seja bem-vindo ao jogo de forca")

    erros = 0
    enforcou = False
    acertou = False
    palavra_secreta = seleciona_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    while (not enforcou and not acertou):
        chute = pegar_letra_informada(letras_acertadas, erros)

        if chute not in palavra_secreta:
            erros += 1
            enforcou = erros == 7
            continue
        
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra
            index += 1

        #enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    if enforcou:
        mensagens.imprime_mensagem_perdedor(palavra_secreta)

    if acertou:
        mensagens.imprime_mensagem_vencedor()

def seleciona_palavra_secreta():
    palavras = utils.ler_arquivo()
    idx = random.randrange(0, len(palavras))

    return palavras[idx].upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pegar_letra_informada(letras_acertadas, erros):
    mensagens.desenha_forca(erros)
    print(letras_acertadas)
    letra = input("Qual letra? ").strip().upper()
    
    return letra

if (__name__ == "__main__"):
    jogar()