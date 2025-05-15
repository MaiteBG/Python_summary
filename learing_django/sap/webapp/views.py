from django.http import HttpResponse


# Create your views here.
def default_view_method(request):
    return HttpResponse("Este es un mensaje de bienvenida")