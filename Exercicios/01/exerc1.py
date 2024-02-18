lado = int(input("Digite o lado do quadrado entre 1 e 20: "))
if 1 <= lado <= 20:
    for i in range(lado):
        for j in range(lado):
            print("*", end=" ")
        print()
else :
    print (' O valor digitado não está entre o intervalo  1 e 20 ')