import sympy as sym 

t = sym.Symbol('t')
s = sym.Symbol('s')

# en dominio tiempo
e2 = sym.exp(2*t)
# escalon unitario
u = sym.Piecewise((0,t<0),(1,t>=0))
uH = sym.Heaviside(t)
# impulso
delta2 = sym.DiracDelta(t-2)

# Transformando a Laplace
e2s = sym.laplace_transform(e2,t,s)
delta2s = sym.laplace_transform(delta2,t,s)
us = sym.laplace_transform(u,t,s)
uHs = sym.laplace_transform(uH,t,s)

# Salida
print('\n f(t) = e**(2t) \n')
sym.pprint(e2)
sym.pprint(e2s)
print('\n f(t) = Dirac delta: \n')
sym.pprint(delta2)
sym.pprint(delta2s)
print('\n f(t) = Piecewise: \n')
sym.pprint(u)
sym.pprint(us)
print('\n f(t) = Heaviside: \n')
sym.pprint(uH)
sym.pprint(uHs)




