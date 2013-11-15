# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=255, help_text='Nombre del propietario', verbose_name='Nombre del propietario')
    delete = models.BooleanField(help_text='Propietario borrado', verbose_name='Borrar propietario')
    
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = "propietario"
        verbose_name_plural = "propietarios"
        permissions = (
            ("manage_owner", "Gestiona los propietarios "),
        )
        
    class Admin:
        save_on_top = True
        
# Clase Grupo/Bandas
class Group(models.Model):
    name = models.CharField(max_length=255, help_text='Nombre del Grupo/Banda', verbose_name='Nombre del grupo')
    delete = models.BooleanField(help_text='Grupo borrado', verbose_name='Borrar grupo')
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = "grupo"
        verbose_name_plural = "grupos"
        permissions = (
            ("manage_group", "Gestiona los grupos - bandas "),
        )
        
    class Admin:
        save_on_top = True
        
# Clase Locales de ensayo
class Premise(models.Model):
    name = models.CharField(max_length=255, help_text='Nombre del local de ensayo', verbose_name=' Nombre')
    description = models.TextField(help_text='Descripción del local de ensayo', verbose_name='Descripción')
    geolocalization = models.TextField(help_text='Iframe de google maps', verbose_name='Iframe de Google maps ')
    active = models.BooleanField(help_text='Usuario activado desactivado', verbose_name='Activar usuario')
    delete = models.BooleanField(help_text='Usuario borrado', verbose_name='Borrar usuario')
    owners = models.ManyToManyField(Owner, blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True, null=True)
    
    class Meta:
        ordering = ['-name']
        verbose_name = "local"
        verbose_name_plural = "locales"
        permissions = (
            ("manage_premise", "Gestiona los locales "),
        )
        
    class Admin:
        save_on_top = True
    
# Clase Material de ensayo
class Material(models.Model):
    name = models.CharField(max_length=255, help_text='Nombre del material de reserva', verbose_name='Nombre del material')
    description = models.TextField(help_text='Descripción del material de reserva', verbose_name='Descripción del material')
    stock = models.SmallIntegerField(help_text='Stock del material', verbose_name='Stock')
    price = models.DecimalField(max_digits=5, decimal_places=4, help_text='Precio del material', verbose_name='Precio')
    delete = models.BooleanField(help_text='Material borrado', verbose_name='Borrar material')
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = "material"
        verbose_name_plural = "materiales"
        permissions = (
            ("manage_material", "Gestiona los materiales de las salas "),
        )
        
    class Admin:
        save_on_top = True
        
# Clase Salas de ensayo
class Room(models.Model):
    name = models.CharField(max_length=255, help_text='Nombre de la sala de ensayo', verbose_name='Nombre de la sala')
    description = models.TextField(help_text='Descripción de la sala de ensayo', verbose_name='Descripción de la sala')
    price = models.DecimalField(max_digits=5, decimal_places=4, help_text='Precio de la sala sin impuestos', verbose_name='Precio de la sala sin impuestos')
    delete = models.BooleanField(help_text='Sala borrada', verbose_name='Borrar sala')
    groups = models.ManyToManyField(Group)
    materials = models.ManyToManyField(Material)
    premise = models.ForeignKey(Premise)
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = "sala de ensayo"
        verbose_name_plural = "salas de ensayo"
        permissions = (
            ("manage_room", "Gestiona las salas de ensayo "),
        )
        
    class Admin:
        save_on_top = True


# Clase Galería de imágenes
class Gallery(models.Model):
    name = models.CharField(max_length=255, help_text='Nombre de la imagen', verbose_name='Nombre')
    title = models.CharField(max_length=255, help_text='Titulo de la imagen', verbose_name='Titulo')
    alt = models.CharField(max_length=255, help_text='Texto alternativo', verbose_name='Texto alternativo')
    path = models.CharField(max_length=255, help_text='Path relativo de la imagen', verbose_name='Ruta de la imagen')
    timestamp = models.DateTimeField(auto_now_add=True, help_text='Marca de tiempo de la imagen')
    image = models.ImageField(upload_to='images')
    delete = models.BooleanField(help_text='Imagen borrada', verbose_name='Borrar imagen')
    group = models.ForeignKey(Group)
    premise = models.ForeignKey(Premise)
    group = models.ForeignKey(Group)
    room = models.ForeignKey(Room)
    material = models.ForeignKey(Material)
    
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "galería"
        verbose_name_plural = "galerías"
        permissions = (
            ("manage_gallery", "Gestiona las galerías de imágenes "),
        )
        
    class Admin:
        save_on_top = True
        
# Clase configuración de los locales
class Setting(models.Model):
    fee = models.BooleanField(help_text='Activar sistema de pagos', verbose_name='Permitir pagar las reservas')
    google_analytics = models.TextField(help_text='Código Google Analytics', verbose_name='Código Google Analytics')
    timezone = models.CharField(max_length=255, help_text='Zona horaria', verbose_name='Zona horaria')
    lang = models.CharField(max_length=2, help_text='Idioma', verbose_name='Idioma')
    tax = models.PositiveSmallIntegerField(help_text='Impuestos', verbose_name='Impuestos (IVA)')
    opening_day_1 = models.BooleanField(help_text='Lunes día de apertura', verbose_name='Abierto lunes')
    opening_hour_ini_1_1 = models.TimeField(help_text='Hora de inicio de apertura mañana', verbose_name='Hora de inicio de apertura mañana')
    opening_hour_end_1_1 = models.TimeField(help_text='Hora de inicio de cierre mañana', verbose_name='Hora de inicio de cierre mañana')
    opening_hour_ini_1_2 = models.TimeField(help_text='Hora de inicio de apertura tarde', verbose_name='Hora de inicio de apertura tarde')
    opening_hour_end_1_2 = models.TimeField(help_text='Hora de inicio de cierre tarde', verbose_name='Hora de inicio de cierre tarde')
    opening_day_2 = models.BooleanField(help_text='Martes día de apertura', verbose_name='Abierto martes')
    opening_hour_ini_2_1 = models.TimeField(help_text='Hora de inicio de apertura mañana', verbose_name='Hora de inicio de apertura mañana')
    opening_hour_end_2_1 = models.TimeField(help_text='Hora de inicio de cierre mañana', verbose_name='Hora de inicio de cierre mañana')
    opening_hour_ini_2_2 = models.TimeField(help_text='Hora de inicio de apertura tarde', verbose_name='Hora de inicio de apertura tarde')
    opening_hour_end_2_2 = models.TimeField(help_text='Hora de inicio de cierre tarde', verbose_name='Hora de inicio de cierre tarde')
    opening_day_3 = models.BooleanField(help_text='Miercoles día de apertura', verbose_name='Abierto miercoles')
    opening_hour_ini_3_1 = models.TimeField(help_text='Hora de inicio de apertura mañana', verbose_name='Hora de inicio de apertura mañana')
    opening_hour_end_3_1 = models.TimeField(help_text='Hora de inicio de cierre mañana', verbose_name='Hora de inicio de cierre mañana')
    opening_hour_ini_3_2 = models.TimeField(help_text='Hora de inicio de apertura tarde', verbose_name='Hora de inicio de apertura tarde')
    opening_hour_end_3_2 = models.TimeField(help_text='Hora de inicio de cierre tarde', verbose_name='Hora de inicio de cierre tarde')
    opening_day_4 = models.BooleanField(help_text='Jueves día de apertura', verbose_name='Abierto jueves')
    opening_hour_ini_4_1 = models.TimeField(help_text='Hora de inicio de apertura mañana', verbose_name='Hora de inicio de apertura mañana')
    opening_hour_end_4_1 = models.TimeField(help_text='Hora de inicio de cierre mañana', verbose_name='Hora de inicio de cierre mañana')
    opening_hour_ini_4_2 = models.TimeField(help_text='Hora de inicio de apertura tarde', verbose_name='Hora de inicio de apertura tarde')
    opening_hour_end_4_2 = models.TimeField(help_text='Hora de inicio de cierre tarde', verbose_name='Hora de inicio de cierre tarde')
    opening_day_5 = models.BooleanField(help_text='Viernes día de apertura', verbose_name='Abierto viernes')
    opening_hour_ini_5_1 = models.TimeField(help_text='Hora de inicio de apertura mañana', verbose_name='Hora de inicio de apertura mañana')
    opening_hour_end_5_1 = models.TimeField(help_text='Hora de inicio de cierre mañana', verbose_name='Hora de inicio de cierre mañana')
    opening_hour_ini_5_2 = models.TimeField(help_text='Hora de inicio de apertura tarde', verbose_name='Hora de inicio de apertura tarde')
    opening_hour_end_5_2 = models.TimeField(help_text='Hora de inicio de cierre tarde', verbose_name='Hora de inicio de cierre tarde')
    opening_day_6 = models.BooleanField(help_text='Sábado día de apertura', verbose_name='Abierto sábado')
    opening_hour_ini_6_1 = models.TimeField(help_text='Hora de inicio de apertura mañana', verbose_name='Hora de inicio de apertura mañana')
    opening_hour_end_6_1 = models.TimeField(help_text='Hora de inicio de cierre mañana', verbose_name='Hora de inicio de cierre mañana')
    opening_hour_ini_6_2 = models.TimeField(help_text='Hora de inicio de apertura tarde', verbose_name='Hora de inicio de apertura tarde')
    opening_hour_end_6_2 = models.TimeField(help_text='Hora de inicio de cierre tarde', verbose_name='Hora de inicio de cierre tarde')
    opening_day_7 = models.BooleanField(help_text='Domingo día de apertura', verbose_name='Abierto domingo')
    opening_hour_ini_7_1 = models.TimeField(help_text='Hora de inicio de apertura mañana', verbose_name='Hora de inicio de apertura mañana')
    opening_hour_end_7_1 = models.TimeField(help_text='Hora de inicio de cierre mañana', verbose_name='Hora de inicio de cierre mañana')
    opening_hour_ini_7_2 = models.TimeField(help_text='Hora de inicio de apertura tarde', verbose_name='Hora de inicio de apertura tarde')
    opening_hour_end_7_2 = models.TimeField(help_text='Hora de inicio de cierre tarde', verbose_name='Hora de inicio de cierre tarde')
    premise = models.OneToOneField(Premise, primary_key=True)
    
    def __str__(self):
        return self.lang
    
    def __unicode__(self):
        return self.lang
    
    class Meta:
        verbose_name = "configuración"
        verbose_name_plural = "configuraciones"
        permissions = (
            ("manage_setting", "Gestiona la configuración del local "),
        )
        
    class Admin:
        save_on_top = True
        
class ExcludedDays(models.Model):
    excluded_day = models.DateField(help_text='Días excluídos', verbose_name='Días a excluir')
    setting = models.ForeignKey(Setting)
    
    def __str__(self):
        return self.excluded_day
    
    def __unicode__(self):
        return self.excluded_day
    
    class Meta:
        verbose_name = "día excluido"
        verbose_name_plural = "días excluidos"
        permissions = (
            ("manage_excluded_days", "Gestiona los días excluidos "),
        )
        
    class Admin:
        save_on_top = True
    
# Clase Propietario del local de ensayo
