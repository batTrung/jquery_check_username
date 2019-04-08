from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import RegisterForm

def register(request):
	form = RegisterForm()

	return render(request,'account/register.html',{'form':form})

def check_username(request):
	data= {}
	username = request.GET.get('username')
	data['is_errors'] = User.objects.filter(username=username).exists()

	return JsonResponse(data)