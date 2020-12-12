
def boas_vindas_msg(msg):
    asteriscos = len(msg) * '*'

    print(asteriscos)
    print(msg)
    print(asteriscos)

def selecionar_dificuldade():
    opcao_invalida = True
    while opcao_invalida:
        print("Selecione o nível de dificuldade do jogo")
        print("1 - Fácil")
        print("2 - Médio")
        print("3 - Dificil")
        print("0 - Desistir do Jogo")

        nivel = int(input("Nível de Dificuldade: "))

        if nivel in [1,2,3]:
            return nivel
        elif nivel == 0:
            print("Até logo")
            exit()
        else:
            print("É necessário informar um nível de dificuldade válido")
