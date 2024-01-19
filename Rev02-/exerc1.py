#1. Implemente um programa em __Python__ faça a seguinte brincadeiras: 
   # * O programa informa que "está pensando" em um número entre 1 e 100 e peça para você adivinhar.
   # * O programa gera então um valor inteiro aleatório entre 1 e 100 (incluindo 1 e 100) e da, no máximo, 8 oportunidades para você adivinhar. 
   # * A cada tentativa o programa responde:
   #     * Não o número é maior (:-(
   #     * Não o número é menor (:-O 
   #     * Parabéns você acertou (:-)
    #    * Lamento, acabaram suas oportunidades (;-)    
    
    
import random

def jogo_adivinhacao():
    numero_escolhido = random.randint(1, 100)
    tentativas = 0
    totalTentativas = 8
    print(' Estou pensando em um numero no intervalo 1 a 100. Tente advinhar ')

    while tentativas < totalTentativas:
        tentativa = int(input('Faça sua ' + str(tentativas + 1) + 'ª Tentativa: '))

        if tentativa < numero_escolhido:
            print(' Não, o número é maior (:-(')

        elif tentativa > numero_escolhido:
            print(' Não, o número é menor (:-O) ')

        elif tentativa == numero_escolhido:
            print('Parabéns, você acertou (:-)')
            break

        tentativas += 1

    if tentativas == totalTentativas:
        print('Lamento, acabaram suas oportunidades (;-)')


jogo_adivinhacao()

        
 
    
    
