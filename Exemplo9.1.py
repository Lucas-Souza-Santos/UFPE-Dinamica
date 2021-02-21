import matplotlib.pyplot
import math

y = 0.0

tempo = []
for x in range(0, 40):
    tempo.append(x)

corrente_armadura = []

exp = math.e

for t in tempo:
  y = math.ceil(800 + 139 * (math.pow(exp, (-1.35 * t))) - 939 * (math.pow(exp, (-0.2 * t))))
  corrente_armadura.append(y)  

matplotlib.pyplot.plot(tempo, corrente_armadura)

print(matplotlib.pyplot.show())



