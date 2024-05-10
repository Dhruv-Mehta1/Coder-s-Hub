from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
	path('user/',views.layout,name='user'),
	path('home',views.home,name='home'),
	path('common_form',views.common_form,name='common_form'),
	path('common_table',views.common_table,name='common_table'),
	path('post_queries',views.post_queries,name='post_queries'),
	path('view_queries',views.view_queries,name='view_queries'),
	path('more_details/<int:id>',views.more_details,name='more_details'),
	path('post_answer/<int:id>',views.post_answer,name='post_answer'),
	path('view_answer',views.view_answer,name='view_answer'),
	path('job_vacancy',views.job_vacancy,name='job_vacancy'),
	path('job_details/<int:id>',views.job_details,name='job_details'),
	path('apply_now/<int:id>',views.apply_now,name='apply_now'),
	path('post_project',views.post_project,name='post_project'),
	path('view_project',views.view_project,name='view_project'),
	path('project_details/<int:id>',views.project_details,name='project_details'),
	path('aboutus',views.aboutus,name='aboutus'),
	path('contact_us',views.contact_us,name='contact_us'),
	path('services',views.services,name='services'),
	path('feedback',views.feedback,name='feedback'),
	path('login_user',views.login_user,name='login_user'),
	path('register_user',views.register_user,name='register_user'),
	path('contactus_store',views.contactus_store,name='contactus_store'),
	path('user_store',views.user_store,name='user_store'),
	path('login_user_chack',views.login_user_chack,name='login_user_chack'),
	path('logout_user',views.logout_user,name='logout_user'),
	path('srore_resume/<int:id>',views.srore_resume,name='srore_resume'),
	path('feedback_store',views.feedback_store,name='feedback_store'),
	path('post_queries_store/<int:id>',views.post_queries_store,name='post_queries_store'),
	path('post_answer_store/<int:id>',views.post_answer_store,name='post_answer_store'),
	path('post_project_store',views.post_project_store,name='post_project_store'),
	path('forgot',views.forgot,name='forgot'),
	path('forgot_password_check',views.forgot_password_check,name='forgot_password_check'),
]

