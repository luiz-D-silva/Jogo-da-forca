from constantes import NIVEL_DIFICULDADE, RANGE_LETRAS
import random
import re
import os


def menu_dificuldade():
    dificuldade = ""
    while not dificuldade:
        for k, v in NIVEL_DIFICULDADE.items():
            print(f'{k} - {v.upper()}')
        dificuldade = input('Escolha um nível de dificuldade: ')
        if dificuldade not in NIVEL_DIFICULDADE.keys():
            print(f'"{dificuldade}" é inválido')
            dificuldade = ""
    return dificuldade


def sorteia_palavra(dificuldade):
    with open('static/words.txt', mode='r') as b_dados:
        lista_palavras = []
        for palavra in b_dados.readlines():
            p = palavra.strip()
            min_, max_ = RANGE_LETRAS[dificuldade]
            if min_ <= len(p) <= max_:
                lista_palavras.append(p)

    max_range = len(lista_palavras)-1
    index = random.randint(0, max_range)
    palavra_sorteada = lista_palavras[index]
    return palavra_sorteada


def calcula_tentativas(palavra_sorteada, dificuldade):
    letras_unicas = set(palavra_sorteada)
    tentativas = 1.5 * len(letras_unicas)
    if dificuldade == "1":
        tentativas += 2
    if dificuldade == "3":
        tentativas -= 2
        tentativas = min(tentativas, 15)
    tentativas = round(tentativas)
    return tentativas


def play(palavra_sorteada, dificuldade):
    tentativas = tentativas_restantes = calcula_tentativas(
        palavra_sorteada, dificuldade)
    estado_atual = ["_" for letra in palavra_sorteada]
    letras_digitadas = []

    letra = ""
    while "_" in estado_atual and tentativas_restantes:
        for char in estado_atual:
            print(char, end=" ")
        print(f'''\n\nTentativa {tentativas - tentativas_restantes +1} de {
            tentativas}''')
        letra = ""
        while not letra:
            letra = input('\nDigite uma letra: ').lower()
            os.system('cls')
            if len(letra) != 1 or not re.match("[a-z]", letra):
                print(f'''"{letra}" é inválido,
                    digite somente e apenas uma letra.''')
                letra = ""

        if letra not in letras_digitadas:
            letras_digitadas.append(letra)
            if letra in palavra_sorteada:
                posicao = [letra.start() for letra in re.finditer(
                    letra, palavra_sorteada)]
                # posicao = []
                # index_posicao = 0
                # for l_ in palavra_sorteada:
                #     if l_ == letra:
                #         posicao.append(index_posicao)
                #     index_posicao += 1
                for value in posicao:
                    estado_atual[value] = letra
            else:
                print(f'a letra "{letra}" não está na palavra\n')
                tentativas_restantes -= 1
        else:
            print(f'"{letra}" já foi diditado')
    return tentativas_restantes
