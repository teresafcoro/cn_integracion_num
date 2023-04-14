import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def punto_medio(f, a, b):
    # función f a integrar y extremos del intervalo de integración a y b
    return (b - a) * f((a + b) / 2)

x = sym.Symbol('x', real = True)
f = lambda x: np.log(x)
a = 1.; b = 3.
print('El valor aproximado es ', punto_medio(f, a, b))
print('El valor exacto es ', float(sym.integrate(sym.log(x), (x, a, b))))

plt.figure()
nodos = np.array([(a + b) / 2])
xp = np.linspace(a, b)

plt.plot(xp, f(xp), 'b', label = 'Área exacta')
plt.plot([a, a, b, b], [f(a), 0, 0, f(b)], 'b')
plt.plot(nodos, f(nodos),'ro', label = 'Puntos de interpolación')

p = np.polyfit(nodos, f(nodos), len(nodos) - 1)
xp = np.linspace(a, b)
yp = np.polyval(p, xp)
plt.plot(xp, yp, 'r--', label = 'Área aproximada')

pa = np.polyval(p, a)
pb = np.polyval(p, b)
plt.plot([a, a, b, b], [pa, 0, 0, pb], 'r--')

plt.legend()
plt.show()
