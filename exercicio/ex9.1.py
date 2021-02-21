import math
import matplotlib.pyplot as plt

Rff = 100
Lff = 50 
Ra = 0.05
La = 0.0005
Kg = 50 
Wm = (1200 * 2 * math.pi) / 60


tempo_f = []
for t in range(0, 100):
    tempo_f.append(t/10)

corrente_campo = []


for t in tempo_f:
    iff = 2.5 - 2.5 * math.pow(math.e, -2 * t)
    corrente_campo.append(iff)

# plt.plot(tempo_f, corrente_campo)
# print(plt.show())

############## Exercício 9.1 Parte B ############
tempo_a = []
for t in range(0, 1000):
    tempo_a.append(t / 100000)

corrente_armadura = []
tensao_carga = []
conjugado = []

for t in tempo_a:
    ia = 200 - 200 * math.pow(math.e, -625 * t)
    vc = 240 - 52.5 * math.pow(math.e, -625 * t)
    Tc = 397.88 * (1 - math.pow(math.e, -625 * t))

    corrente_armadura.append(ia)
    tensao_carga.append(vc)
    conjugado.append(Tc)

# plt.plot(tempo_a, corrente_armadura)
plt.plot(tempo_a, tensao_carga)
# plt.plot(tempo_a, conjugado)

print(plt.show())