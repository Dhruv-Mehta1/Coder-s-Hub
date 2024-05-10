from django.db import models

# Create your models here.

class Technology(models.Model):
	tech_name = models.CharField(max_length = 70)
	date = models.DateField(auto_now = True)

	class Meta:
		db_table = 'tech_table'

class Subtechnology(models.Model):
	subtech_name = models.CharField(max_length = 80)
	tech = models.ForeignKey(Technology,on_delete=models.CASCADE)
	date = models.DateField(auto_now = True)

	class Meta:
		db_table = 'subtech_table'

