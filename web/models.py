from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager , PermissionsMixin 
from .enumeraciones import *
# Create your models here.

class Usuariomanager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError("El correo es obligatorio")
        usuario = self.model(correo=self.normalize_email(correo), **extra_fields)
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_gerente", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo=correo, password=password, **extra_fields)   
    
    
class Usuario(AbstractBaseUser,PermissionsMixin):
    correo = models.EmailField("correo", max_length=150 , primary_key=True)
    nombre = models.CharField("nombre", max_length=50)
    is_staff = models.BooleanField("empleado",default=False)
    is_gerente = models.BooleanField("gerente",default=False)
    is_superuser = models.BooleanField("superuser",default=False)
    es_baneado = models.BooleanField("baneado", default=False)
    
    USERNAME_FIELD="correo"
    objects=Usuariomanager()
    REQUIRED_FIELDS=["nombre"]
    

class Promocion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='promociones/')
    validada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class Hotel(models.Model):
    nombre=models.CharField(max_length=50, null=False ,unique=True)
    descripción=models.CharField(max_length=150, null=False)
    foto=models.ImageField(upload_to='hotel',null=False)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Habitacion(models.Model):
    TIPOS_DE_HABITACION = [
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('SUITE', 'Suite'),
    ]
    
    hotel=models.ForeignKey("web.Hotel", verbose_name=("hotel"), on_delete=models.CASCADE)
    numero_habitacion = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto=models.ImageField(upload_to='foto_h',null=True,default="null")
    cantidad_habitaciones = models.IntegerField()
    cantidad_banos = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPOS_DE_HABITACION, default='SINGLE')
    precio=models.IntegerField(default=0, validators=[MinValueValidator(0),MaxValueValidator(999999)])
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'Habitación {self.numero_habitacion} - {self.nombre}'
    
class Reserva(models.Model):
    usuario = models.ForeignKey("web.Usuario", verbose_name=("usuario"), on_delete=models.CASCADE)
    habitacion = models.ForeignKey("web.Habitacion", verbose_name=("habitacion"), on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return f'Reserva de {self.usuario} en {self.habitacion.nombre}'
