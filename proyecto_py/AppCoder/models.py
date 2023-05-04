from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Viaje(models.Model):

    nombre=models.CharField(max_length=50)
    personas=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.personas}"

class Suscriptor(models.Model):

    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"

class Menus(models.Model):

    nombre=models.CharField(max_length=50)
    ingredientes=models.CharField(max_length=100)
    personas=models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.ingredientes} {self.personas}"
    
class Comentarios(models.Model):

    nombre=models.CharField(max_length=50)
    reseña=models.CharField(max_length=140)
    estrellas=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.reseña} {self.estrellas}"
    
class Avatar(models.Model):
        imagen=models.ImageField(upload_to="avatars")
        user=models.ForeignKey(User, on_delete=models.CASCADE)
