# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from simpleform.models import form1

def index(request):
	return HttpResponse("Hello, world. You're at the index.")

def entryform(request):
	return render(request,'simpleform/formtemplate.html')

def thanks(request):
	#a=request.POST['f_name']
	p=form1(First_Name=request.POST['f_name'],Last_Name=request.POST['l_name'],DOB=request.POST['dob'],Course=request.POST['course'])
	p.save()
	return HttpResponse("Data Entered!!")