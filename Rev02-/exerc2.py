#Implemente um programa em __Python__ faça a seguinte brincadeiras: 
 #   * O programa pede para você pensar em um número entre 1 e 100 que ele vai adivinhar.
  #  * Você pensa em um valor inteiro aleatório entre 1 e 100 (incluindo 1 e 100) e o programa tem, no máximo, 8 oportunidades para você adivinhar. 
   # * A cada tentativa o programa o computador pergunta para vc se:
    #* Não o número é maior (:-(
     #   * Não o número é menor (:-O 
      #  * Parabéns você acertou (:-)
    #* Se exceder as 8 tentativas sem acertar o computador resoponde:
    #    * Que pena, acabaram minhas oportunidades (;-). Qual foi o número que você pensou?
    #* O computador deve verificar se sua resposta anteriores estão corretas e, casso você tenha enganado a aplicação ele retorna:
     #   * Você trapaceou (:-(. o número x não é maior/menor que meu chute y. 
      #  Substitua x pelo valor pensado pelo usuário, y pelo valor tentativo dado pelo computador e maior ou menor pela resposta dada por você e que estava incorreta.  


import random

def jogo_adivinhacao():
    numero_usuario = random.randint(1, 100)
    tentativas = 0
    total_tentativas = 8
    
    print("Vou tentar advinhar um número que voçê pensar entre 1 e 100!")

    while tentativas < total_tentativas:
        mpalpite = random.randint(1, 100)
    
    if tentativas == numero_usuario:
        print("Parabéns! Você acertou (:-) ")
        break
    elif tentativas < numero_usuario:
        print("Não, o número é maior (:-(")
    else:
        print("Não, o número é menor (:-O)")

    tentativas += 1

    if tentativas == total_tentativas:
        print(f"Lamento, acabaram suas oportunidades (;-)")
        print(f"O número correto era {numero_usuario}.")

if __name__ == "__main__":
    jogo_adivinhacao()
