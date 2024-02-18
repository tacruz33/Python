# Formatação de Strings


nome = 'Tales'
altura = 1.74
peso = 95

imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura' # arredondar valor inteiro (:.3f) quantas casas decimais desejadas. O virgula tbm divide os valores em mil,milhão e etc.
linha_2=  f'pesa {peso} quilos e seu imc é {imc:.3f}'
print (linha_1)
print (linha_2)


