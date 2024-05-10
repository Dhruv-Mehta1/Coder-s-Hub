from django.contrib import admin
from django.urls import path
from myadmin import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/',views.layout,name='myadmin'),
    path('dashboard/',views.deshbord,name='dashboard'),
    path('common_form/',views.common_form,name='common_form'),
    path('add_technology/',views.add_technology,name='add_technology'),
    path('add_technology_store',views.add_technology_store,name='add_technology_store'),
    path('delete_technology/<int:id>',views.delete_technology,name='delete_technology'),
    path('update_technology/<int:id>',views.update_technology,name='update_technology'),
    path('sub_technology/',views.sub_technology,name='sub_technology'),
    path('subtech_store',views.subtech_store,name='subtech_store'),
    path('common_table/',views.common_table,name='common_table'),
    path('view_technologys/',views.view_technologys,name='view_technologys'),
    path('view_subtechnologys/',views.view_subtechnologys,name='view_subtechnologys'),
    path('delete_subtechnology/<int:id>',views.delete_subtechnology,name='delete_subtechnology'),
    
    path('users/',views.users,name='users'),
    path('details_user/<int:id>',views.details_user,name='details_user'),
    path('view_company/',views.view_company,name='view_company'),
    path('details_company/<int:id>',views.details_company,name='details_company'),

    
    path('view_project/',views.view_project,name='view_project'),
    path('project_user/<int:id>',views.project_user,name='project_user'),
    path('details_pro/<int:id>',views.details_pro,name='details_pro'),
    path('view_feedback/',views.view_feedback,name='view_feedback'),
    
    path('view_inquiry/',views.view_inquiry,name='view_inquiry'),
    path('edit_technology/<int:id>',views.edit_technology,name='edit_technology'),
    path('edit_subtechnology/<int:id>',views.edit_subtechnology,name='edit_subtechnology'),
    path('update_subtechnology/<int:id>',views.update_subtechnology,name='update_subtechnology'),
    path('login/',views.login,name='login'),
    path('login_check',views.login_check,name='login_check'),
    path('logout/',views.logout,name='logout'),
]