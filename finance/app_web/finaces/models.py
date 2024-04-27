import datetime
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.utils import timezone


    

class clientes(models.Model):
    #como puedo factorizar los datos en una sola clase 
    nombre = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    email = models.EmailField(null = True, blank = True)
    celular = models.CharField(max_length = 20)
    password = models.CharField(max_length=128)  # Campo para la contraseña encriptada
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null = True, blank = True)

    def save(self, *args, **kwargs):
        # Encriptar la contraseña antes de guardar
        if not self.pk:
            self.password = make_password(self.password)
        super(clientes, self).save(*args, **kwargs)

    #Convetir a acdena para que los datos se visualicen 
    #def __str__(self):
    #    return f" {self.email}-{self.}"


class Producto(models.Model):
    nombr_producto = models.CharField(max_length = 50) 
    abreviatura = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 100)
    #ident_number = models.CharField(max_length = 12, blank = True) # blank = true que acaepte valores null
    #Crear una llave foranea 
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null = True, blank = True)

class cliente_producto(models.Model):
    #id = models.CharField(max_length = 20)
    numero_cuenta= models.IntegerField()
    #id_cliente_Producto = models.ForeignKey(clientes,Producto, on_delete = models.CASCADE)
    id_cliente = models.ForeignKey(clientes, on_delete = models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null = True, blank = True)
    

class Tipo_transancciones(models.Model):
    nombre = models.CharField(max_length = 50) 
    abreviatura = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null = True, blank = True)
   
class Transaccion(models.Model):
    monto = models.IntegerField() 
    id_cliente_producto = models.ForeignKey(cliente_producto, on_delete = models.CASCADE)
    id_transaccion = models.ForeignKey(Tipo_transancciones, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null = True, blank = True)








