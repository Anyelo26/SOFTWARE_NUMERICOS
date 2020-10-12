def fv(t):
    #suponemos que son coeficientes
    
    cn=0
    resp=0
    while cn<=arra(len):
        resp=resp+arra(cn)*t**(arra(len)-cn)
        cn+=cn+1
    return resp

def f(x):
    return x**3 - 2 *x**2 -1


def biseccion():
    
    #arra=arr
    a =0
    b =4
    #a = limi
    #b = limis
    error=10
    i=0

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
        error=abs(fc)
        i=i+1

        print("raiz ",i,"raiz obtenida:","{0:.6f}".format(raiz))

#print("{0:.6f}".format(raiz))
biseccion()