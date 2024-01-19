import random

def jogo_adivinhacao():
    numero_pensado = random.randint(1, 100)
    total_tentativas = 8
    tentativas = 0

    print('Pense em um número entre 1 e 100, vou tentar adivinhar!')

    while tentativas < total_tentativas:
        palpite = random.randint(1, 100)

        resposta = input(f"É {palpite}? (Digite 's' se eu acertei, 'm' se o número é maior, 'men' se o número é menor): ")

        if resposta.lower() == 's':
            print('Parabéns, eu acertei! (:-)')
            return
        elif resposta.lower() == 'm':
            print(f'Não, o número é maior (:-(')
        elif resposta.lower() == 'men':
            print(f'Não, o número é menor (:-O)')
        else:
            print(f'Opção inválida. Digite "s", "m" ou "men".')

        tentativas += 1

    print(f'Que pena, acabaram minhas oportunidades (;-). Qual foi o número que você pensou?')
    numero_usuario = int(input('Digite o número que você pensou: '))

    if numero_usuario != numero_pensado:
        print(f'Você trapaceou (:-(). O número {numero_pensado} não é {"" if numero_pensado > numero_usuario else "menor "}{"maior" if numero_pensado > numero_usuario else "menor"} que o meu chute {numero_usuario}.')
    else:
        print('Você realmente pensou no número', numero_pensado, '! Eu não consegui adivinhar dessa vez.')

# Chame a função para executar o jogo
jogo_adivinhacao()
