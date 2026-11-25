from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(
        validators=[
            MinValueValidator(18),
            MaxValueValidator(60)
        ]
    )



