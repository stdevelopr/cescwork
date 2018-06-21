from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def work_detail(request, id):
	return render(request, 'work_detail.html', {'id':id})