from django.contrib import admin
from django.urls import path
from company import views

urlpatterns = [
	
    path('company/',views.layout,name='company'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_vacancy/',views.add_vacancy,name='add_vacancy'),
    path('add_vacancy_store',views.add_vacancy_store,name='add_vacancy_store'),
    path('view_vacancy/',views.view_vacancy,name='view_vacancy'),
    path('delete_vacancy/<int:id>',views.delete_vacancy,name='delete_vacancy'),
    path('vacancy_details/<int:id>',views.vacancy_details,name='vacancy_details'),
    path('edit_vacancy/<int:id>',views.edit_vacancy,name='edit_vacancy'),
    path('vacancy_update/<int:id>',views.vacancy_update,name='vacancy_update'),
    path('job_applications/',views.job_applications,name='job_applications'),
    path('application_details/<int:id>',views.application_details,name='application_details'),


    path('login_company/',views.login_company,name='login_company'),
    path('registation_company/',views.registation_company,name='registation_company'),
    path('registation_company_store',views.registation_company_store,name='registation_company_store'),
    path('login_company_chack',views.login_company_chack,name='login_company_chack'),
    path('logout_company',views.logout_company,name='logout_company'),
    path('forgot/',views.forgot,name='forgot'),
    path('forgot_password_check',views.forgot_password_check,name='forgot_password_check'),

]