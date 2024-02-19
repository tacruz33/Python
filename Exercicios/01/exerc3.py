#Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

notas_1= int(input(" Digite sua primeira nota do bimestre : "))
notas_2= int(input(" Digite sua segunda nota do bimestre : "))
notas_3= int(input(" Digite sua terceira nota do bimestre : "))
notas_4= int(input(" Digite sua quarta nota do bimestre : "))

media_bimestral = float((notas_1 + notas_2+ notas_3 + notas_4) / 4)

print ( " Sua média dos 4 bimestres é : ", media_bimestral)