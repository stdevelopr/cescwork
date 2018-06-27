from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Work

# Create your views here.
def home(request):
	works = Work.objects.filter(status=True)
	return render(request, 'home.html', {"works":works})

def work_detail(request, id):
	try:
		work = Work.objects.get(id=id)
	except Work.DoesNotExist:
		return redirect('/')
	return render(request, 'work_detail.html', {'work':work})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password=password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	form = UserCreationForm()
	context = {'form' :form}
	return render(request, 'registration/register.html', context)
