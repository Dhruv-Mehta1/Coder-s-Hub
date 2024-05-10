from django.shortcuts import render,redirect
from django.http import HttpResponse
from company.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from user.models import Resume,Profile_user
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import send_mail
import os
# Create your views here.
def layout(request):
	return render(request,'company/layout.html')

def dashboard(request):
	return render(request,'company/dashboard.html')

def add_vacancy(request):
	context={}
	return render(request,'company/add vacancy.html',context)

def add_vacancy_store(request):
	Tite = request.POST['jobtitle']
	Description = request.POST['desc']
	Job_type = request.POST['jobtype']
	Location = request.POST['location']
	nov = request.POST['nov']
	Min_salary = request.POST['minsalary']
	Experience = request.POST['exprience']
	Date = request.POST['date']
	id = request.user.id
	Add_new_vacancy.objects.create(Tite = Tite,Description = Description,Job_type = Job_type,Location = Location,No_of_vacancy = nov,Min_salary = Min_salary,Experience = Experience,Date = Date,user_id = id)
	return redirect('/company/add_vacancy/')

def view_vacancy(request):
	result = Add_new_vacancy.objects.all()
	context = {'result':result}
	return render(request,'company/view_vacancy.html',context)

def delete_vacancy(request,id):
	result = Add_new_vacancy.objects.get(id=id)
	result.delete()
	return redirect('/company/view_vacancy')

def vacancy_details(request,id):
	result = Add_new_vacancy.objects.get(id=id)
	context = {'result':result}
	return render(request,'company/vacancy_details.html',context)

def edit_vacancy(request,id):
	result = Add_new_vacancy.objects.get(id=id)
	context={'result':result}
	return render(request,'company/edit_vacancy.html',context)

def vacancy_update(request,id):
	data = {
		'Tite' : request.POST['jobtitle'],
		'Description' : request.POST['desc'],
		'Job_type' : request.POST['jobtype'],
		'Location' : request.POST['location'],
		'No_of_vacancy' : request.POST['nov'],
		'Min_salary' : request.POST['minsalary'],
		'Experience' : request.POST['exprience'],
		'Date' : request.POST['date'],
	}
	Add_new_vacancy.objects.update_or_create(id=id,defaults=data)
	return redirect('/company/view_vacancy')

def job_applications(request):
	result = Resume.objects.all()
	context = {'result':result}
	return render(request,'company/job_applications.html',context)

def application_details(request,id):
	result = Resume.objects.get(id=id)
	result1 = Profile_user.objects.all()
	context = {'result':result,'result1':result1}
	return render(request,'company/application_details.html',context)

def login_company(request):
	context = {}
	return render(request,'company/login_company.html',context)

def registation_company(request):
	context = {}
	return render(request,'company/registation_company.html',context)

def registation_company_store(request):
	companyname =  request.POST['cname']
	ownername = request.POST['ownername']
	email = request.POST['email']
	number = request.POST['number']
	address = request.POST['address']
	acompany=request.POST['acompany']
	password = request.POST['pass']
	cpassword = request.POST['cpass']
	username = request.POST['uname']
	if password == cpassword:
		user = User.objects.create_user(first_name=companyname,last_name=ownername,email=email,password=password,username=username)
		Profile_company1.objects.create(phone_number=number,address=address,about_comoany=acompany,user_id=user.id,password=password)
		return redirect("/company/login_company")
	else:
		return redirect('/user/registation_company')

def login_company_chack(request):
	username = request.POST['uname']
	password = request.POST['password']

	result = auth.authenticate(request,username=username,password=password)
	if result is None:
		return redirect('/company/login_company/')
	else:
		auth.login(request,result)
		return redirect('/company/dashboard')

def logout_company(request):
	auth.logout(request)
	return redirect('/company/login_company')

def forgot(request):
	context = {}
	return render(request,'company/forgotpass.html',context)

def forgot_password_check(request):
	myemail = request.POST['email']

	if User.objects.filter(email=myemail).exists():
		result = User.objects.get(email=myemail)
		id = result.id
		profile = Profile_company1.objects.get(user_id=id)
		password = profile.password

		subject = 'Welcome to Coders Hub'
		message = f'Your Password is {password}'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [myemail, ]

		send_mail( subject, message, email_from, recipient_list )
		return redirect('/company/login_company')

