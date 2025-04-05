from django.db import models
from django.contrib.auth.models import User

class Navigators(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

class Mentorados(models.Model):
    estagio_choices = (
        ('I', 'Iniciante'),
        ('M', 'Intermediário'),
        ('A', 'Avançado'),
    
    )
    nome = models.CharField( max_length=255)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    criado_em = models.DateField(auto_now_add=True)
    navigators = models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.CASCADE)
    estagios = models.CharField(max_length=2, choices=estagio_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    estagio_choices = estagio_choices


    def __str__(self):
        return self.nome
