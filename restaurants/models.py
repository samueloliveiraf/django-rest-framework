from django.db import models
from django.contrib.auth import get_user_model

from localflavor.br.br_states import STATE_CHOICES

# Create your models here.


User = get_user_model()


class Restaurant(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=200)
    address = models.CharField(verbose_name='Endereço', max_length=250)
    number = models.CharField(verbose_name='Número', max_length=20)
    area = models.CharField(verbose_name='Bairro', max_length=100)
    city = models.CharField(verbose_name='Cidade', max_length=100)
    state = models.CharField(verbose_name='Estado', max_length=2, choices=STATE_CHOICES)
    phone = models.CharField(verbose_name='Contato', max_length=14)
    email = models.EmailField(verbose_name='E-mail', blank=True, null=True)
    owner = models.ForeignKey(User, verbose_name='Proprietário', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'
    
    def __str__(self):
        return self.name


class Dish(models.Model):
    resutaurant = models.ForeignKey(Restaurant, verbose_name='Restaurante', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nome', max_length=100)
    description = models.TextField(verbose_name='Descrição')
    price = models.DecimalField(verbose_name='Preço', max_digits=19, decimal_places=2)
    photo = models.ImageField(verbose_name='Foto', upload_to='photos')

    class Meta:
        verbose_name = 'Prato'
        verbose_name_plural = 'Pratos'
    
    def __str__(self):
        return self.name


class Order(models.Model):
    MONEY = 'MN'
    DEBIT_CARD = 'DC'
    CREDIT_CARD = 'CC'
    PAYMENT_CHOICES = (
        (MONEY, 'Dinheiro'),
        (DEBIT_CARD, 'Cartão de Débito'),
        (CREDIT_CARD, 'Cartão de Crédito'),
    )
    restaurant = models.ForeignKey(Restaurant, verbose_name='Restaurante', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='Cliente', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, verbose_name='Prato', on_delete=models.CASCADE)
    payment = models.CharField(verbose_name='Forma de Pagamento', max_length=2, choices=PAYMENT_CHOICES)
    quantity = models.PositiveBigIntegerField(verbose_name='Quantidade')
    total = models.DecimalField(verbose_name='Total do Pedido', max_digits=19, decimal_places=2)
    ordered_at = models.DateTimeField(verbose_name='Data do Pedido', auto_now_add=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return self.user.first_name
