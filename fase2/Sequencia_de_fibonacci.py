f = int(input("Digite um número inteiro para calcular a sequência de Fibonacci: "))
sequencia = []
a = 1.618
b = 2.236
for i in range(f):
    sequencia.append(round((pow(a, i))/b))

print(*sequencia, sep=", ")