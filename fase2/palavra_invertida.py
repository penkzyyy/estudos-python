palavra = input("Insere uma palavra para a veres invertida: ")
count = len(palavra)
invertida = ""
while count > 0:
    invertida += palavra[count - 1]
    count -= 1

print("A palavra invertida é: ", invertida)