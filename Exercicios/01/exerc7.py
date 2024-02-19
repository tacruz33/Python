'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. '''

real_hora = float(input("Digite quanto você ganha por hora : "))
horas_trabalhadas = float(input("Digite quantas horas trabalhar por dia : "))

salario = horas_trabalhadas * real_hora

print (" Seu salário é : ", salario)