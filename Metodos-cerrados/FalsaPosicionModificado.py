def f(x):
    return 3*x**3 + 2*x +2

def falsaPosicion():
    # Este metodo necesita el Polinomio
    # tambien 2 puntos extremos, "xi" y "xs"
    # y un posible contador de repeticiones,
    # en este caso estamos usando "error"

    xi = -1
    xs = -1/2
    numeroIteraciones=6
    i=0

    ranterior=0
    error=100

    contenedor=[]           #arreglo contenedor contenedor principal
    valores=[0,0,0,-1]      #arreglo contenedor secundario valores[xi,xs,iteracions,error]
    while numeroIteraciones> 0: #si el error es mayor de 4 decimales
        valores[0]=xi
        valores[1]=xs
        fxi=f(xi)
        fxs=f(xs)

        ractual=(  xi*fxs-xs*fxi  )/(  fxs-fxi  )
        cond=fxi*fxs

        if cond<0:
            xs=ractual
        elif cond>=0:
            xi=ractual
        
        if i!=0:
            error=abs(((ractual - ranterior)/ractual)*100)
        ranterior=ractual
        i=i+1
        numeroIteraciones=numeroIteraciones-1        
        
        valores[2]=ractual 
        valores[3]=error
        contenedor.append(valores)                
        dibujaMatriz(contenedor)
        


def dibujaMatriz(M):
    for i in range(len(M)):
        print ('[')
        for j in range(len(M[i])):
            print ('{:>3s}'.format(str(M[i][j])))
        print (']')

falsaPosicion()

