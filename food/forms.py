from django import forms
from .models import Food
from pyuploadcare.dj.forms import ImageField


class FoodForm(forms.ModelForm):
    class Meta:
        image = ImageField(label='')
        model = Food
        fields = ('title', 'description', 'portion', 'price', 'tag', 'delivery_time', 'image')
