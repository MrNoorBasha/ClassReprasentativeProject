"""collegedata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from ksrm import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('welcome/',views.welcome,name='welcome'),

    path('Student_submit/',views.student_submit,name='submit'),
 	path('Student_records/',views.student_records,name='display'),
 	path('Student_show/<int:id>',views.student_show,name='view'),
 	path('Student_delete/<int:id>',views.student_delete,name='delete'),
	path('Student_update/<int:id>',views.student_update,name='update'),

    path('Professor_submit/',views.professor_submit, name='professor'),
    path('Professor_records/',views.professor_records, name = 'professor_records'),
    path('Professor_show/<int:id>',views.professor_show, name = 'professor_show'),
    path('Professor_delete/<int:id>',views.professor_delete,name='professor_delete'),
	path('Professor_update/<int:id>',views.professor_update,name='professor_update'),

    
    path('accounts/',include('allauth.urls')),
    path('google/',TemplateView.as_view(template_name='ksrm/login.html'))


]
