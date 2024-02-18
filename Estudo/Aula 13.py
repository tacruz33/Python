''' Formatação de Strings


nome = 'Tales'
altura = 1.74
peso = 95

imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura' # arredondar valor inteiro (:.3f) quantas casas decimais desejadas. O virgula tbm divide os valores em mil,milhão e etc.
linha_2=  f'pesa {peso} quilos e seu imc é {imc:.3f}'
print (linha_1)
print (linha_2)'''


# Método Format

a= 'A'
b = 'B'
c = 1.1
string = 'a={0} b={1} c={2:.2f}' # pegando por indicie os valores, desta forma não necessito ter ordem.
formato = string.format(a, b, c)

print (formato)