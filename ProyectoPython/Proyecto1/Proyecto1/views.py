from django.http import HttpResponse
from django.template import Template, Context

def probando_template(request):
    html = open("C:\\Users\\jp_lu\\OneDrive\\Escritorio\\ProyectoCoder\\Plantillas\\template1.html")
    plantilla = Template(html.read())
    html.close()
    contexto = Context()
    documento = plantilla.render(contexto)              
    return HttpResponse(documento)

def saludo(request):
    return HttpResponse("Hola Django-Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Esta es la segunda vista")
