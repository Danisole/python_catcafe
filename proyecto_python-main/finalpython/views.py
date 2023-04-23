from django.http import HttpResponse
from django.template import Template, Context, loader



# def probandoPlantilla(request):
#     archivo=open(r"C:\Users\Usuario\Desktop\final-python-coder\finalpython\Plantillas\template1.html")
#     texto=archivo.read()
#     archivo.close()

#     template = Template(texto)
#     contexto = Context()
#     documento =template.render(contexto)

#     return HttpResponse(documento)

def probandoPlantilla(request):
   
    diccionario={ "lista":[1,2,3,4,5,6,7,8]}
   
    template = loader.get_template("template1.html")
    documento=template.render(diccionario)

    return HttpResponse(documento)


def saludar(request):
    return HttpResponse("hola mundo cruel")