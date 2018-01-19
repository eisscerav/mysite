from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=20)
    age = forms.IntegerField(label='Age')
    gender = forms.CharField(label='Gender', max_length=20)