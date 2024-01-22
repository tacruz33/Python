# Inicializando um dicionário para armazenar os votos de cada jogador
votos = {}


while True:
    try:
        numero_jogador = int(input("Número do jogador (0=fim): "))

        if numero_jogador == 0:
            break

        if 1 <= numero_jogador <= 23:
            votos[numero_jogador] = votos.get(numero_jogador, 0) + 1
        else:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")

    except ValueError:
        print("Por favor, digite um número válido.")


total_votos = sum(votos.values())


print("\nResultado da votação:\n")
print(f"Foram computados {total_votos} votos.\n")

print("Jogador Votos           %")
for jogador, votos_jogador in sorted(votos.items()):
    percentual = (votos_jogador / total_votos) * 100
    print(f"{jogador}               {votos_jogador}               {percentual:.1f}%")


melhor_jogador = max(votos, key=votos.get)
votos_melhor_jogador = votos[melhor_jogador]
percentual_melhor_jogador = (votos_melhor_jogador / total_votos) * 100


print(f"\nO melhor jogador foi o número {melhor_jogador}, com {votos_melhor_jogador} votos, correspondendo a {percentual_melhor_jogador:.1f}% do total de votos.")