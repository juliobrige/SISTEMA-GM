from django.db import models
from django.contrib.auth.models import User


class navigatiors(models.Model):
    nome = models.models.CharField(max_length=255)
    user = model.models.ForeignKey(user, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

class Mentorados(models.Model):

    estagio_choices = (
        ('E1', '10-100k'),
        ('E2', '10-1kk')
    )
    nome = models.models.CharField( max_length=255)
    foto = models.models.ImageField(upload_to='fotos', null=True, blank=True)
    criado_em = models.models.DateField(auto_now_add=True)
    navigators = models.models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.CASCADE)
    user = model.models.ForeignKey(user, on_delete=models.CASCADE)
    estagios=models.models.CharField(max_length=2, choice=estagio_choices )


    def __str__(self):
        return self.nome
