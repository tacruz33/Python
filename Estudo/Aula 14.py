# If/ elif .. else

'''entrada =  input( ' Você quer "entrar" ou "sair"')

if entrada == 'entrar':
    print (' Vocẽ entrou no sistema')
elif entrada == 'sair':
    print (' Vocẽ saiu do sistema')
else :
    print(" Você não digitou nem entrar e nem sair")'''
    
primeiro_valor = input('Digite um valor : ')
segundo_valor = input ("Digiter outro valor : ")

if primeiro_valor > segundo_valor:
    print (" O primeiro valor e maior que o segundo")
elif primeiro_valor < segundo_valor:
    print (' O segundo valor e maior que o primeiro')
elif primeiro_valor == segundo_valor:
    print(' Os valores são iguais ')
else :
    print (' erro')