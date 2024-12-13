
#funcion que convierte a carecteres string un polinomio
######################
#import sympy 
#x,y,z=sympy.symbols('x y z')		#declaracion de variables
#expr=input("ingrese funcion en terminos de x ")	#almacenamiento de polinomio
#print(sympy.sympify(expr).subs(x,1))	#impresion de evaluacion de expresion del polinomio, asgnando el valor de x = 1 

######################
#from math import *
#import sympy as sp 
#from scipy.misc import derivative		#importacion de derivada


#########################
#Prueba derivada y evaluacion numerica		
#f = lambda x: derivada()					#evaluacion de derivada en x
#print(derivative(f,0, dx=1e-8))			

#########################
#Funcion prueba despejada
#def pol_prima(x): 					
#    return (10*x +5)**(1/3)		
#    return (2*x +1)**(1/3)			
    
#def puntofijo(f, p0, tol, n): #Método del punto fijo
#    i = 1				

#pol(x), po = 0.9, tol = 10^-10, n=100

#print("Pol prueba")
#puntofijo(pol_prima, 1, 0.0001, 12)
#puntofijo(pol_prima, 0, 0.00001, 12)

#from sympy.parsing.sympy_parser import parse_expr
#var=parse_expr("1/2")
#print(var)





######################33
#	parte funcional 
#
#############################
from sympy.parsing.sympy_parser import parse_expr									#conversor de String-Funcion
from sympy.parsing.sympy_parser import standard_transformations						#importacion de Conversor a String
from sympy.parsing.sympy_parser import implicit_multiplication_application			#importacion de Transformation estandar para polinomio

transformations=(standard_transformations+(implicit_multiplication_application,))	#almacenamiento de conversion a polinomio + 

var=parse_expr("y**2+3x",transformations=transformations)	#variable que trabaja con String, y la conversion del polinomio
print(var)		#impresion del polinomio.


########################################
### Funcion encargada de convertir linea de caracteres a string para conversion a polinomio

polinomio="x^2+3x^3+2x^7"

def condic(pol): #funcion que detecta caracteres
	return pol.find("^")    # retorna posicion de caracter, -1 si no se encuentra

def conversion(pol): #funcion recursiva de concatenamiento de nuevo String para polinomio
	eo=condic(pol)
	if eo<0:
		return pol
	else:
		temp1=pol[0:eo]
		temp2=pol[eo+1:len(pol)]
		pol=temp1+"**"+temp2
		
	return conversion(pol)  #retorna String polinomio cambiado
var=conversion(polinomio)
print(var)

