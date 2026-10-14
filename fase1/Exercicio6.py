numero1 = int(input("Coloque a sua primeira nota (de 1 a 5)"))
numero2 = int(input("Coloque a sua segunda nota (de 1 a 5)"))
numero3 = int(input("Coloque a sua terceira nota (de 1 a 5)"))

nota = int((numero1 + numero2 + numero3) / 3)

if ( nota >=3): 
 print("A sua media e: ",nota, "e esta aprovado")
else:
 print("A sua media e: ",nota, "e esta reprovado")
