import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def plotting(f, a, b, nodos):
    plt.figure()
    xp = np.linspace(a,b) # 50 puntos
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

def trapecio(f, a, b):
    plotting(f, a, b, np.array([a, b]))
    return (b - a) * (f(a) + f(b)) / 2

def trapecio_comp(f, a, b, n): 
    x = np.linspace(a, b, n + 1)
    s = 0.
    for i in range(n):
        s += trapecio(f, x[i], x[i + 1])
    return s  

x = sym.Symbol('x', real = True)
f = lambda x: np.log(x)
a = 1.; b = 3. ; n = 4
print('El valor aproximado es', trapecio_comp(f, a, b, n))
print('El valor exacto es', float(sym.integrate(sym.log(x), (x, a, b))))
