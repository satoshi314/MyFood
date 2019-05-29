from django.forms import ModelForm
from django import forms
from .models import Shop


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'evaluate', 'station', 'genre','url','photo','coordinate','state']
        
#フォームでクラス定義⇒単純にgetメソッドを採用        
#class SearchForm(forms.Form):
#    url=forms.CharField()