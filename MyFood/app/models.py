from django.db import models
from django.contrib.auth.models import User


class State(models.Model):
    message  =   models.CharField(max_length=30)
    symbol =   models.ImageField(blank=True,upload_to='system')  
    def __str__(self):
        return self.message    #この記述をすることでオブジェクトの呼び名が指定した要素になる
    
class Shop(models.Model):    
    name = models.CharField(max_length=30)
    evaluate = models.FloatField(blank=True)
    station = models.CharField(max_length=30,blank=True)
    genre = models.CharField(max_length=30,blank=True)
    url = models.CharField(max_length=200,blank=True)
    comment = models.CharField(max_length=300,blank=True)
    photo =models.ImageField(blank=True,upload_to='photos')
    coordinate = models.CharField(max_length=30,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name


