import sympy
x,y,z=sympy.symbols('x y z')

var= input("Introduce la Función en terminos de x:")
print(sympy.sympify(var))
y=eval(var)

print("y={}".format(y))
