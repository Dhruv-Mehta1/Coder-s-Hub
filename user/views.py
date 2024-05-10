from django.shortcuts import render,redirect
from django.http import HttpResponse
from myadmin.models import Technology,Subtechnology
from company.models import Add_new_vacancy
from user.models import *
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
import os

# Create your views here.

def layout(request):
	return render(request,'user/layout.html')

def home(request):
	return render(request,'user/home.html')

def common_form(request):
	return render(request,'user/common_form.html')

def common_table(request):
	return render(request,'user/common_table.html')

def post_queries(request):
	result1 = Technology.objects.all()
	result2 = Subtechnology.objects.all()
	context = {'tech':result1,'subtech':result2}
	return render(request,'user/post_queries.html',context)

def post_queries_store(request):
	title = request.POST['title']
	subtech = request.POST['subtech']
	tech = request.POST['tech']
	description = request.POST['desc']
	file = request.FILES['f']
	id = request.user.id 
	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(file.name,file)
	Post_query.objects.create(title=title,tech_id=tech,subtech_id=subtech,description=description,file=file.name,user_id=id)
	return redirect('/user/post_queries')

def view_queries(request):
	result = Post_query.objects.all()
	context = {'result':result}
	return render(request,'user/view_queries.html',context)

def more_details(request,id):
	result = Post_query.objects.get(id=id)
	context = {'result':result}
	return render(request,'user/more_details.html',context)

def post_answer(request,id):
	context = {'que_id':id}
	return render(request,'user/post_answer.html',context)

def post_answer_store(request,id):
	answer = request.POST['ans']
	user_id = request.user.id
	Answer.objects.create(answer=answer,user_id=user_id,que_id=id)
	return redirect('/user/view_answer')

def view_answer(request):
	result = Answer.objects.all()
	context = {'result':result}
	return render(request,'user/view_answer.html',context)

def job_vacancy(request):
	result = Add_new_vacancy.objects.all()
	context = {'result':result}
	return render(request,'user/job_vacancy.html',context)

def job_details(request,id):
	result = Add_new_vacancy.objects.get(id=id)
	context = {'result':result}
	return render(request,'user/job_details.html',context)

def apply_now(request,id):
	context = {'vacancy_id' : id}
	return render(request,'user/apply_now.html',context)

def srore_resume(request,id):
	file = request.FILES['resume']
	user_id = request.user.id
	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')
	obj = FileSystemStorage(location=mylocation)
	obj.save(file.name,file)
	Resume.objects.create(file = file.name,user_id = user_id,vacancy_id=id)
	return redirect('/user/job_vacancy')

def post_project(request):
	result = Technology.objects.all()
	result1 = Subtechnology.objects.all()
	context = {'tech':result,'subtech':result1}
	return render(request,'user/post_project.html',context)

def post_project_store(request):
	title = request.POST['title1']
	abstract = request.POST['abstract']
	desc = request.POST['desc']
	database = request.POST['database']
	tool = request.POST['tool']
	mydoc = request.FILES['doc1']
	source = request.FILES['source']
	subtech = request.POST['subtech']
	tech = request.POST['tech']
	id = request.user.id
	mylocation = os.path.join(settings.MEDIA_ROOT,'upload')

	obj = FileSystemStorage(location=mylocation)
	obj.save(mydoc.name,mydoc)
	obj.save(source.name,source)
	Project_upload.objects.create(title=title,abstract=abstract,description=desc,database=database,tool=tool,document=mydoc.name,sourcecode=source,subtech_id=subtech,tech_id=tech,user_id=id)
	return redirect('/user/view_project')	

def view_project(request):
	result = Project_upload.objects.all()
	context = {'result':result}
	return render(request,'user/view_project.html',context)

def project_details(request,id):
	result = Project_upload.objects.get(id=id)
	context = {'result':result}
	return render(request,'user/project_details.html',context)

def aboutus(request):
	return render(request,'user/aboutus.html')

def contact_us(request):
	return render(request,'user/contactus.html')

def contactus_store(request):
	name = request.POST['name']
	email = request.POST['email']
	number = request.POST['number']
	message = request.POST['message']
	Contactus.objects.create(name=name,email=email,phone_no=number,message=message)
	return redirect("/user/contact_us")

def services(request):
	return render(request,'user/services.html')

def feedback(request):
	return render(request,'user/feedback.html')

def feedback_store(request):
	rate = request.POST['rate']
	message = request.POST['message']
	id = request.user.id
	Feedback.objects.create(rate=rate,message=message,user_id=id)
	return redirect("/user/feedback")

def login_user(request):
	return render(request,'user/login_user.html')

def register_user(request):
	return render(request,'user/register_user.html')

def user_store(request):
	fname = request.POST['fname']
	lname = request.POST['lname']
	email = request.POST['email']
	number = request.POST['number']
	gender = request.POST['gender']
	dob = request.POST['dob']
	address = request.POST['address']
	password = request.POST['password']
	cpassword = request.POST['re_pass']
	uname = request.POST['uname']
	if password == cpassword:
		user = User.objects.create_user(first_name=fname,last_name=lname,email=email,password=password,username=uname)
		Profile_user.objects.create(phone_number=number,address=address,gender=gender,date_of_birth=dob,user_id=user.id,password=password)
		return redirect('/user/login_user')
	else:
		return redirect('user/register_user')

def login_user_chack(request):
	uname = request.POST['uname']
	password = request.POST['password']
	result = auth.authenticate(request,username=uname,password=password)

	if result is None:
		error_msg = "Invalid Username Or Password"
		return render(request,'user/login_user.html',{'error' : error_msg})
	else:
		auth.login(request,result)
		return redirect('/user/home')

def logout_user(request):
	auth.logout(request)
	return redirect('/user/home')


def forgot(request):
	context = {}
	return render(request,'user/forgot.html',context)

def forgot_password_check(request):
	myemail = request.POST['email']

	if User.objects.filter(email=myemail).exists():
		result = User.objects.get(email=myemail)
		id = result.id
		profile = Profile_user.objects.get(user_id=id)
		password = profile.password

		subject = 'Welcome to Coders Hub'
		message = f'Your Password is {password}, do not share Any One'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [myemail, ]

		send_mail( subject, message, email_from, recipient_list )
		return redirect('/user/login_user')


	else:
		message.success(request,'Email not Found in Database')
		return redirect('/user/forgot')