import random
import utils.util as utils
import utils.mensagens as mensagens

erros = 0

def jogar():
    utils.boas_vindas_msg("Olá seja bem-vindo ao jogo de forca")

    enforcou = False
    acertou = False
    palavra_secreta = seleciona_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    while (not enforcou and not acertou):
        chute = pegar_letra_informada(letras_acertadas)

        if chute not in palavra_secreta:
            registra_erro()
            continue
        
        index = 0
        for letra in palavra_secreta:
            if chute == letra:
                letras_acertadas[index] = letra

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

    if enforcou:
        mensagens.imprime_mensagem_perdedor()

    if acertou:
        mensagens.imprime_mensagem_vencedor()

def seleciona_palavra_secreta():
    palavras = utils.ler_arquivo()
    idx = random.randrange(0, len(palavras))

    return palavras[idx].upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def registra_erro():
    erros += 1

def pegar_letra_informada(letras_acertadas):
    mensagens.desenha_forca(erros)
    print(letras_acertadas)
    letra = input("Qual letra? ").strip().upper()
    
    return letra

if (__name__ == "__main__"):
    jogar()