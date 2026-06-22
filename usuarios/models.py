from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('consultor', 'Consultor'),
    ]
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='consultor')

    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"
        
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.get_or_create(usuario=instance)