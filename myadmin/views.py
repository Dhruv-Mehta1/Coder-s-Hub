from django.shortcuts import render,redirect
from django.http import HttpResponse
from myadmin.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from user.models import Profile_user,Project_upload,Contactus,Feedback
from company.models import Profile_company1
# Create your views here.
def layout(request):
	return render(request,'myadmin/layout.html')

def deshbord(request):
	return render(request,'myadmin/dashboard.html')

def common_form(request):
	return render(request,'myadmin/common_Foarm.html')

def common_table(request):
	return render(request,'myadmin/common_table.html')

def add_technology(request):
	return render(request,'myadmin/add_technology.html')

def add_technology_store(request):
	mytech = request.POST['tech_name']
	Technology.objects.create(tech_name=mytech)
	return redirect('/myadmin/add_technology')

def view_technologys(request):
	result = Technology.objects.all()
	context = {'result':result}
	return render(request,'myadmin/view_technologys.html', context)

def delete_technology(request,id):
	result = Technology.objects.get(id=id) # id for take Porticular selected data 
	result.delete()  #delete() to delete data
	return redirect('/myadmin/view_technologys/')
	
def edit_technology(request,id):
	result = Technology.objects.get(id=id)
	contaxt = {'result' : result}
	return render(request,'myadmin/edit_technology.html',contaxt)

def	update_technology(request,id):
	mytech_name = request.POST['tech_name']
	data = {'tech_name': mytech_name,}
	Technology.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/view_technologys/')


def sub_technology(request):
	result = Technology.objects.all()
	contaxt = {'techno':result}
	return render(request,'myadmin/sub_technology.html',contaxt)

def subtech_store(request):
	mytechid = request.POST['techid']
	mysubtech = request.POST['Subtech']
	Subtechnology.objects.create(tech_id=mytechid,subtech_name=mysubtech)
	return redirect('/myadmin/sub_technology')

def view_subtechnologys(request):
	result = Subtechnology.objects.all()
	context = {'result':result}
	return render(request,'myadmin/view_subtechnologys.html',context)

def delete_subtechnology(request,id):
	result = Subtechnology.objects.get(id=id) # id for take Porticular selected data 
	result.delete()  #delete() to delete data
	return redirect('/myadmin/view_subtechnologys/')

def edit_subtechnology(request,id):
	technology = Technology.objects.all()
	result = Subtechnology.objects.get(id=id)
	context = {'result':result,'technology':technology}
	return render(request,'myadmin/edit_subtechnology.html',context)

def	update_subtechnology(request,id):
	mytechid = request.POST['techid']
	mysubtech = request.POST['Subtech']
	data = {'tech_id': mytechid,
			'subtech_name':mysubtech}
	Subtechnology.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/view_subtechnologys/')


def users(request):
	result = Profile_user.objects.all()
	context = {'result':result}
	return render(request,'myadmin/users.html',context)

def details_user(request,id):
	result = Profile_user.objects.get(id=id)
	context = {'result':result}
	return render(request,'myadmin/details_user.html',context)

def view_company(request):
	result = Profile_company1.objects.all()
	context = {'result':result}
	return render(request,'myadmin/view_company.html',context)

def details_company(request,id):
	result = Profile_company1.objects.get(id=id)
	context = {'result':result}
	return render(request,'myadmin/details_company.html',context)


def view_project(request):
	result = Project_upload.objects.all()
	context = {'result':result}
	return render(request,'myadmin/view_project.html',context)

def project_user(request,id):
	result = Project_upload.objects.get(id=id)
	result1 = Profile_user.objects.get(id=id)
	context = {'result':result,'result1':result1}
	return render(request,'myadmin/project_user.html',context)

def details_pro(request,id):
	result = Project_upload.objects.get(id=id)
	context = {'result':result}
	return render(request,'myadmin/details_pro.html',context)

def view_feedback(request):
	result = Feedback.objects.all()
	context = {'result':result}
	return render(request,'myadmin/view_feedback.html',context)

def view_inquiry(request):
	result = Contactus.objects.all()
	context = {'result':result}
	return render(request,'myadmin/view_inquiry.html',context)




def login(request):
	context = {}
	return render(request,'myadmin/login.html',context)

def login_check(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(request,username=username,password=password)
	if user is None:
		print("invalid email or password")
		return redirect("/myadmin/login")
	else:
		auth.login(request,user)
		return redirect("/myadmin/dashboard/")

def logout(request):
	auth.logout(request)
	return redirect('/myadmin/login')