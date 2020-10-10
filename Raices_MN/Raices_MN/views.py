from django.http import HttpResponse
import datetime
def saludo(request): #Primera vista
    documento="""<html>
    <body>
    <h1>
    "Hola mundo!."
    </h1>
    </body>
    </html>"""
    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego..")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)