#Implementación del método del punto fijo

from math import *
import sympy as sp 




"""
#Prueba derivada
def derivada():
    x = sp.Symbol('x')
    y = (10*x +5)**(1/3)
    return sp.diff(y,x)

print(derivada())
"""
#Funcion prueba
def pol_prima(x): 
    return (10*x +5)**(1/3)
    
def puntofijo(f, p0, tol, n): #Método del punto fijo
    i = 1
    while i <= n:
        p = f(p0)
        print("Iter= ", "%03d" % i, "; p =", "%.14f" % p)
        if abs(p-p0) < tol:
            print("Error final:"," %.6f" % abs(p-p0))
            return p
        p0 = p
        i +=1
    print("Iteraciones agotadas:Error!")
    return 

#pol(x), po = 0.9, tol = 10^-10, n=100

print("Pol prueba")
puntofijo(pol_prima, 1, 0.0001, 12)
