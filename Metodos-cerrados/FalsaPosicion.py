
def f(x):
    return 3*x**3 + 2*x +2

xi = -1
xs = -1/2
numeroIteraciones=6
i=0

ranterior=0
error=100

while numeroIteraciones> 0: #si el error es mayor de 4 decimales
    print("{0:.6f}".format(xi))
    print("{0:.6f}".format(xs))
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
    #print("{0:.6f}".format(ranterior))
    
    print("raiz","{0:.6f}".format(ractual))
    print("iteracion",i,"porcentaje de error:","{0:.6f}".format(error))

#print("{0:.6f}".format(raiz))
