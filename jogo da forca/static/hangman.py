from defs import menu_dificuldade, sorteia_palavra, play
dificuldade = menu_dificuldade()
palavra_sorteada = sorteia_palavra(dificuldade)
player_wins = play(palavra_sorteada, dificuldade)

if player_wins:
    print(f'Parabéns, vc acertou\n A palavra era "{palavra_sorteada}"')
else:
    print(f'Vc perdeu, a palavra era "{palavra_sorteada}"')