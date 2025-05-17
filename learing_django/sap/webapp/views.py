from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from modelsapp.forms import PersonaForm
from modelsapp.models import Persona
# Create your views here.
def index_view(request):
    num_personas = Persona.objects.count()
    personas_data = Persona.objects.order_by('id')
    return render(request, 'index.html', {'num_personas':num_personas, 'personas_data': personas_data})

def detalles(request, id):
    persona = get_object_or_404(Persona, pk = id)
    personaF = PersonaForm(request.POST, instance=persona,  editable = False)

    return render(request, 'detalles.html', {'persona': personaF})


def add_person(request):
    if request.method == 'POST':
        personaF = PersonaForm(request.POST)
        if personaF.is_valid():
            personaF.save()
            return redirect("index")
        else:
            print(personaF.errors)
    else:
        personaF =  PersonaForm()
    return render(request, 'add_person.html', {'persona': personaF})



def update_person(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        personaF = PersonaForm(request.POST, instance=persona)
        if personaF.is_valid():
            personaF.save()
            return redirect("index")
        else:
            print(personaF.errors)
    else:
        personaF = PersonaForm(instance=persona)
        return render(request, 'update_person.html', {'persona': personaF})



def delete_person(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect("index")
