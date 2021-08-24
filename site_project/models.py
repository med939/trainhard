from django.db import models
from django.conf import settings


class Item(models.Model):
    image_1 = models.ImageField(null = True, blank = True, upload_to = 'images/')
    image_2 = models.ImageField(null = True, blank = True, upload_to = 'images/')
    image_3 = models.ImageField(null = True, blank = True, upload_to = 'images/')
    title = models.CharField(max_length = 100, verbose_name='Produit' )
    price = models.FloatField(verbose_name = 'Prix')
    choix = (
        ('Maquillage','Maquillage'),
        ('Parfum homme', 'Parfum homme'),
        ('Parfum femme', 'Parfum femme'),
    
    )
    category = models.CharField(max_length=50, null = True, blank = True, choices = choix, verbose_name='Catégorie')
    description = models.TextField(max_length = 800, null = True, blank = True, verbose_name='déscription')
    additional_information = models.TextField(max_length = 800, null = True, blank = True, verbose_name='Information additionnelle')
    
    
    def __str__(self):
        return self.title
    
    


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add = True)
    orderd_date = models.DateTimeField()
    orderd = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username