from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):# to create your password.
    return render(request, 'generator/home.html')

def about(request):# to create your about page.
    return render(request, 'generator/about.html')

def password(request):
   
   characters = list('abcdefghijklmnopqrstuvwxyz')
   
   if request.GET.get('uppercase'):#thosetup the uppercase
      characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

   if request.GET.get('special'):#thosetup the specialcharacter
      characters.extend(list('!@*#@$%^&'))

   if request.GET.get('numbers'):#thosetup the specialcharacter
      characters.extend(list('0123456789'))

 # una setup a password policies such length with default of 5 char when entering password
   length = int(request.GET.get('length',5))

   thepassword = ''
   for x in range(length):
       thepassword += random.choice(characters)

   return render(request, 'generator/password.html', {'password': thepassword})