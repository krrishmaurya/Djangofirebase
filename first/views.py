
from django.shortcuts import redirect, render
from django.views import View
import info
from . import forms
class Home(View):
    def get(self,request):
        return render(request,'basic.html')


class Singup(View):
    def get(self,request):
        content={
            'signup':forms.Signup()
        }
        return render(request,'signup.html',content)
    
    
    def post(self,request):

        username=request.POST['username']
        email=request.POST['email'] 
        password=request.POST['password']
        user=info.auth.create_user_with_email_and_password(email,password) 
        print(user)
        return redirect('/')



class Login(View):
    def get(self,request):
        content={
            'login_form':forms.Login()

        }        
        return render(request,'login.html',content)

    def post(self,request):
        email=request.POST['email'] 
        password=request.POST['password']
       

        login =info.auth.sign_in_with_email_and_password(email, password)
         
        return redirect('/')    

          




