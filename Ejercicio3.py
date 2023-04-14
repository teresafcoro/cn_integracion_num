import numpy as np
import sympy as sym

def punto_medio(f, a, b):
    return (b - a) * f((a + b) / 2)

def trapecio(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

def simpson(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))

def punto_medio_comp(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    s = 0.
    for i in range(n):
        s += punto_medio(f, x[i], x[i + 1])
    return s

def trapecio_comp(f, a, b, n): 
    x = np.linspace(a, b, n + 1)
    s = 0.
    for i in range(n):
        s += trapecio(f, x[i], x[i + 1])
    return s

def simpson_comp(f, a, b, n): 
    x = np.linspace(a, b, n + 1)
    s = 0.
    for i in range(n):
        s += simpson(f, x[i], x[i + 1])
    return s

def gauss(f, a, b, n):
    [x, w] = np.polynomial.legendre.leggauss(n)
    return np.sum(w * f((b - a) / 2 * x + (b + a) / 2)) * (b - a) / 2

def grado_de_precision(formula, n):
    f = lambda x: np.log(x)
    i = 0
    error = 0.
    x = sym.Symbol('x', real = True)
    while i < 20 and error < 1.e-10:
        f = lambda t: t**i
        error = np.abs(float(sym.integrate(x**i, (x, 1, 3))) - formula(f, 1, 3, n))
        i += 1
        print('f(x) = x^' + str(i-1), '   error = ', error)
    print('\nEl grado de precisión de la fórmula es ', i - 2)

print('\n----  Fórmula del punto medio (1 punto) ----\n')
grado_de_precision(punto_medio_comp, 1)

print('\n----  Fórmula del trapecio (2 puntos) ----\n')
grado_de_precision(trapecio_comp, 1)

print('\n----  Fórmula de Simpson (3 puntos) ----\n')
grado_de_precision(simpson_comp, 1)

print('\n----  gauss n = 1 ----\n')
grado_de_precision(gauss, 1)

print('\n----  gauss n = 2 ----\n')
grado_de_precision(gauss, 2)

print('\n----  gauss n = 3 ----\n')
grado_de_precision(gauss, 3)
