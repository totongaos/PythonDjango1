from django.shortcuts import render
from .form import RegistrationForm
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
# Create your views here.
def index(request):
   return render(request, 'pages/home.html')
def contact(request):
   return render(request, 'pages/contact.html')

def error(request, exception):
   return render(request, 'pages/error.html', {'message': exception})

def register(request):
   form = RegistrationForm()
   #nếu user chọn nút đăng ký
   if request.method == 'POST':
      # gọi những data từ input ở UI vào biến form ở trên
      form = RegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/')

   return render(request, 'pages/register.html', {'form': form})