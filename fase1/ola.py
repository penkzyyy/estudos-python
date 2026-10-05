nome = input("Como te chamas? ")
idade = int(input("Quantos anos tens? "))
ano_nasc = int(input("Em que ano nasceste? "))
import datetime
ano_atual = int(datetime.date.today().year)
print("Olá", nome)
print("Tens neste momento", ano_atual - ano_nasc, "anos" )
print("Daqui a 10 anos terás", idade + 10 , "anos")