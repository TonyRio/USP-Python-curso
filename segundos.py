seg = input("Digite a quantidade de segundos que deseja converter:")
segTot = int(seg)
a = segTot // 86400
segRes = segTot % 86400

b = segRes // 3600
segRes = segTot % 3600

c = segRes // 60
segRes = segTot % 60

d = segRes



print(f" A Conversão de {segTot} segundos ficará :")
print(f"{a} dias , {b} horas, {c} minutos e {d} segundos ")
