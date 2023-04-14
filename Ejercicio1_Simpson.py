import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def simpson(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

x = sym.Symbol('x', real = True)
f = lambda x: np.log(x)
a = 1.; b = 3.
print('El valor aproximado es ', simpson(f, a, b))
print('El valor exacto es ', float(sym.integrate(sym.log(x), (x, a, b))))

plt.figure()
nodos = np.array([a, (a + b) / 2, b])
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
