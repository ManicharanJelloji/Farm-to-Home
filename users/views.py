from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.



def register(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		form = UserRegisterForm()
		if request.method == 'POST':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		return render(request, 'users/register.html', {'form':form})


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				# fname = user.first_name
				return redirect('store')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'users/login.html', context)



def logoutUser(request):
	logout(request)
	return redirect('login')


@ login_required
def profile(request):
	context = {}
	return render(request, 'users/profile.html', context)


