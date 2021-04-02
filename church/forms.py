from django import forms


class VisitorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    address = forms.CharField(required=True)
    city = forms.CharField(required=False)
    about_you = forms.TextInput()