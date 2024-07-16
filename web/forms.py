from typing import Any
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm ,UserChangeForm ,PasswordChangeForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout , Submit , Div ,Field ,HTML,Row,Column
from crispy_forms.bootstrap import PrependedText

useru = get_user_model()

class loginForm(AuthenticationForm):
    pass

class createUser(UserCreationForm):

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={"id":"password1"}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={"id":"password2"}))
    
    class Meta:
        model = useru 
        fields =["correo","nombre"]

    def __init__(self, *args , **kwargs ):
        super().__init__(*args, **kwargs)
        self.helper= FormHelper()
        self.helper.form_method="post"
        self.helper.form_class="needs-validation"
        self.helper.attrs={"novalidate":""}
        self.helper.layout=Layout(
           Field("correo",id="correo") ,
           Field("nombre",id="nombre"),  
           Field("password1",id="contraseña"), 
           Field("password2",id="repetirContraseña")    
        )

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nombre', 'descripción', 'foto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foto'].widget.attrs.update({'accept': 'image/*'})
        
class HabitacionFilterForm(forms.Form):
    TIPOS_DE_HABITACION = [
        ('', 'Todos'),  # Opción para mostrar todas las habitaciones
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('SUITE', 'Suite'),
    ]
    
    tipo = forms.ChoiceField(label='Tipo de Habitación', choices=TIPOS_DE_HABITACION, required=False)
    mostrar_solo_disponibles = forms.BooleanField(label='Mostrar solo disponibles', required=False, initial=False)
    
    def __init__(self, *args, **kwargs):
        super(HabitacionFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('submit', 'Filtrar'))
        
    def filter_queryset(self, queryset):
        tipo = self.cleaned_data.get('tipo')
        mostrar_solo_disponibles = self.cleaned_data.get('mostrar_solo_disponibles')
        
        if tipo:
            queryset = queryset.filter(tipo=tipo)
        if mostrar_solo_disponibles:
            queryset = queryset.filter(disponible=True)
        return queryset
    
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_inicio', 'fecha_fin']  # Agrega 'habitacion' al formulario

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Obtiene el usuario del argumento 'user' pasado desde la vista
        super().__init__(*args, **kwargs)
        # Añade clases CSS de Bootstrap o estilos personalizados si es necesario
        self.fields['fecha_inicio'].widget.attrs.update({'class': 'form-control datetimepicker-input'})
        self.fields['fecha_fin'].widget.attrs.update({'class': 'form-control datetimepicker-input'})

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.usuario = self.user  # Asigna el usuario actual al campo 'usuario' de la reserva
        if commit:
            instance.save()
        return instance
    
class PromocionForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = ['nombre', 'descripcion', 'imagen', 'validada']

    def __init__(self, *args, **kwargs):
        super(PromocionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar cambios'))