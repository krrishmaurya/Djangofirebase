from django import forms



class Signup(forms.Form):
    username=forms.CharField(max_length=20)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())



class Login(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())