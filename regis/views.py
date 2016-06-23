from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	context_dict={}
	return render(request, 'regis/index.html', context_dict)

@login_required
def profile(request):
	return render(request,'regis/profile.html')
