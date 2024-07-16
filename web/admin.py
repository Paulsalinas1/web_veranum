from django.contrib import admin
from .models import *

# Register your models here.
class admHotel(admin.ModelAdmin):
    list_display = ['id' ,'nombre']
    #list_editable
    
class admHabitacion(admin.ModelAdmin):
    list_display = ['id' ,'nombre','tipo']
    #list_editable
    
class admPromo(admin.ModelAdmin):
    list_display = ['id' ,'nombre','validada']
    #list_editable
    
class admUser(admin.ModelAdmin):
    list_display = ['correo' ,'nombre']
    #list_editable
    
admin.site.register(Usuario, admUser)
admin.site.register(Promocion, admPromo)
admin.site.register(Habitacion, admHabitacion)
admin.site.register(Hotel, admHotel)