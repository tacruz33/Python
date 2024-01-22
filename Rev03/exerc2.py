'''2. Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada partida do campeonato. Para isto, faz-se necessário o 
desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de 
programação __Python__. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, 
indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 
Após o final da votação, o programa deverá exibir:

* O total de votos computados;
* Os números e respectivos votos de todos os jogadores que receberam votos;
* O percentual de votos de cada um destes jogadores;
* O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. 

Por exemplo:

Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.'''

# Inicializando um dicionário para armazenar os votos de cada jogador
votos = {0}*23


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