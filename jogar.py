import adivinhacao
import forca
import utils.util as utils

def iniciar():
    utils.boas_vindas_msg("Bem vindo ao Py_Jogos")

    print("----JOGOS----")
    print("(1) Adivinhação")
    print("(2) Forca")
    print("(0) Não quero jogar")
    opcao_jogo = int(input("Qual iremos jogar? "))

    if opcao_jogo == 1:
        adivinhacao.jogar()
    elif opcao_jogo == 2:
        forca.jogar()
    elif opcao_jogo == 0:
        exit()
    else:
        print("Opção de jogo invalida! Reinicie o jogo")

if (__name__ == "__main__"):
    iniciar()