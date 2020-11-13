from django.http import HttpResponse
import datetime
from django.template import Template, Context
from Raices_MN.form import PreguntaForm


def homeMetodo(request): #Primera vista de método
    nombreMet = "NewtonR"
    #Abrimos el doc de plantilla html
    documento= open("C:/Users/ARACELI/Documents/GitHub/Raices_MN/Raices_MN/plantillas/home.html")
    #Carga el documento en una variable de tipo Template
    template = Template(documento.read())
    #Cerrar el documento externo
    documento.close()
    #Crear un contexto
    contexto = Context({"nombreMetodo": nombreMet})
    #Renderizar el documento
    docRend = template.render(contexto)

    return HttpResponse(docRend)

def despedida(request):

    return HttpResponse("Hasta luego..")

def pregunta_crear(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('plantillas/formulario.html')
    else:
           form = PreguntaForm()
    return render(request, 'plantillas/formulario.html', {'form': form},)

