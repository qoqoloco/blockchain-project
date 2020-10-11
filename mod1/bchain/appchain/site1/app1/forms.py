from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from app1.models import Users
from django import forms


class Usersform(ModelForm):
    class Meta:
        model = Users
        fields = ['name','email','phone']
        labels = {'name' : _('shem'),}
        help_text = {'name':('enter hear your name')}

class Userloginform(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput)
