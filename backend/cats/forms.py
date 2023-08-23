from django import forms
from .models import AboutCats

class CatsSearch(forms.ModelForm):
    # text = forms.CharField(label = "text")
    # age = forms.IntegerField(label = "age")
    class Meta:
        model = AboutCats
        fields = ("name","breed","age")
    

    
class CatsForm(forms.ModelForm):
    class Meta:
        model = AboutCats
        fields = ("name","breed","age","image")
