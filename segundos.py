seg = input("Entre com os segundos que deseja converter: ")
tseg = int(seg)
hor = tseg // 3600
sgsRes = tseg % 3600
min = sgsRes //60
segResFin = sgsRes %60

print(f" {hor} horas, {min} minutos e {segResFin} segundos")