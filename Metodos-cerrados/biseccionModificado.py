def f(x):
    return x**3 - 2 *x**2 -1

def biseccion():    
    # Este metodo necesita el Polinomio
    # tambien 2 limites, "a" y "b"
    # y un posible contador de repeticiones,
    # en este caso estamos usando "error"
    a =0        #limites 
    b =4        #limites
    
    #Control para la cantidad de repeticiones, 
    #si se desea tantas iteraciones, 
    #se puede cambiar por una varibale numerica que los contenga
    #

    error=10    # error
    i=0         #Contador
    contenedor=[]       #arreglo contenedor contenedor[raices]
    while error> 1e-6: #si el error es mayor de 4 decimales
        c=(a+b)/2
        fa=f(a)
        fc=f(c)
        if fc==0:
            raiz=c
            break
        elif fa*fc<0:
            b=c
        else:
            a=c
        raiz=c
        error=abs(fc)   #valor absoluto
        contenedor.append(raiz)
        i=i+1
    print (contenedor)
    #for j in contenedor:
        #print("raiz ",j,"raiz obtenida:","{0:.6f}".format(contenedor))

biseccion()

##############################
#def fv(t):
    #suponemos que son coeficientes    
#    cn=0
#    resp=0
#    while cn<=arra(len):
#        resp=resp+arra(cn)*t**(arra(len)-cn)
#        cn+=cn+1
#    return resp
##############################