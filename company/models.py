from django.db import models
from django.contrib.auth.models import User
from myadmin.models import Technology,Subtechnology

# Create your models here.
class Add_new_vacancy(models.Model):
	Tite = models.CharField(max_length=50)
	Description = models.TextField()
	Job_type = models.CharField(max_length=50)
	Location = models.TextField()
	No_of_vacancy = models.CharField(max_length=50)
	Min_salary = models.TextField()
	Experience = models.CharField(max_length=50)
	Date = models.DateField(auto_now=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE,default='')

	class Meta:
		db_table = 'add_new_vacancy'

class Profile_company1(models.Model):
	phone_number = models.BigIntegerField()
	address      = models.TextField()
	about_comoany = models.TextField()
	date = models.DateField(auto_now=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	password = models.CharField(max_length=20)

	class Meta:
		db_table = 'company_profile1'
