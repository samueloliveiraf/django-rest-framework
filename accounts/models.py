from django.db import models
from django.contrib.auth import get_user_model

from localflavor.br.br_states import STATE_CHOICES


User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Endereço', max_length=200)
    number = models.CharField(verbose_name='Número', max_length=20)
    area = models.CharField(verbose_name='Bairro', max_length=100)
    city = models.CharField(verbose_name='Cidade', max_length=100)
    state = models.CharField(verbose_name='Estado', max_length=2, choices=STATE_CHOICES)
    complement = models.TextField(verbose_name='Complemento', blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
    
    def __str__(self):
        return self.user.first_name