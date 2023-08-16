import random
import re

NIVEL_DIFICULDADE = {
    "1": "fácil",
    "2": "normal",
    "3": "difícil"
}

RANGE_LETRAS = {
    "1": (3, 5),
    "2": (6, 9),
    "3": (10, 100)
}

dificuldade = ""
while not dificuldade:
    for k, v in NIVEL_DIFICULDADE.items():
        print(f'{k}-->{v.upper()}')
    dificuldade = input('Escolha o nível de dificuldade: ')
    if dificuldade not in NIVEL_DIFICULDADE.keys():
        print(f'a opção "{dificuldade}" é inválida')
        dificuldade = ""
with open('static/words.txt', mode='r') as banco_dados:
    lista_palavras = []
    for palavra in banco_dados.readlines():
        p = palavra.strip()
        min_, max_ = RANGE_LETRAS[dificuldade]
        if min_ <= len(p) <= max_:
            lista_palavras.append(p)

max_range = len(lista_palavras)-1
index = random.randint(0, max_range)
palavra_sorteada = lista_palavras[index]
print(palavra_sorteada)

letras_unicas = set(palavra_sorteada)
tentativas = 1.5 * len(letras_unicas)
if dificuldade == "1":
    tentativas += 2
elif dificuldade == "3":
    tentativas -= 2
    tentativas = min(14, tentativas)
tentativas = round(tentativas)

letras_digitadas = []
estado_atual = ["_" for char in palavra_sorteada]
while "_" in estado_atual:
    for char in estado_atual:
        print(char, end=" ")
    letra = ""
    while not letra:
        letra = input('Digite uma letra: ')
        if len(letra) != 1 or not in re
        if letra not in letras_digitadas:
            letras_digitadas.append(letra)
            if letra in palavra_sorteada:
                print('---', letra)
            else:
                tentativas -= 1
                print(f'A letra {letra} não está na palavra digitada')
        else:
            print(f'A letra {letra} já foi digitada.')