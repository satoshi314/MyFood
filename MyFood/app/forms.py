from django.forms import ModelForm
from django import forms
from .models import Shop


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'evaluate', 'station', 'genre','url','photo','coordinate','state']
        
#�t�H�[���ŃN���X��`�˒P����get���\�b�h���̗p        
#class SearchForm(forms.Form):
#    url=forms.CharField()