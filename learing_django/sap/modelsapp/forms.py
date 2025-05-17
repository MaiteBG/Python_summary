from django.forms import ModelForm, EmailInput

from modelsapp.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

    def __init__(self, *args, editable=True, **kwargs):
        super().__init__(*args, **kwargs)
        if not editable:
            for field in self.fields.values():
                field.disabled = True  # Desactiva todos los campos