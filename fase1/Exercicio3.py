numero = float(input("Digite um número inteiro: "))
while numero != int(numero):
    print("O número digitado não é um inteiro. Tente novamente.")
    numero = float(input("Digite um número inteiro: "))
    inteiro = int(numero)
    antecessor = int(inteiro - 1)
    sucessor = int(inteiro + 1)
print("O número antecessor de", inteiro, "é", antecessor, "e o sucessor é", sucessor)

