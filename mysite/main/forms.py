from django import forms

class CreateNewList(forms.Form):
    Name = forms.CharField(label="Name", max_length=200)
    Check = forms.BooleanField(required=False)