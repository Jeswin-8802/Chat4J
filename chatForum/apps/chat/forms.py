from django import forms

from django.core.validators import RegexValidator

class CreateForumForm(forms.Form):
    image = forms.ImageField(required = False)
    name = forms.CharField(max_length = 50, validators = [RegexValidator('^(?=.{5,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$', message = '2 <= length <= 50, only numeric, alphabetic, underscore and dot allowed')])
    description = forms.CharField(min_length = 10, max_length = 100)