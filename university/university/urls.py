"""university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.show_instructor_data, name="login"),
    #path('', views.show_student_data, name="home"),
    path('add_student_course/', views.add_student_enrolment, name="add_student_course"),
    path('update_student_email/', views.update_student_email, name="update_student_email"),
    path('delete_student_course/<sid>/<cid>/', views.delete_student_enrolment),

    path('add_instructor_course/', views.add_instructor_enrolment, name="add_instructor_course"),
    path('update_instructor_email/', views.update_instructor_email, name="update_instructor_email"),
    path('delete_instructor_course/<iid>/<cid>/<term>/<year>/', views.delete_instructor_enrolment)

    #path('', TemplateView.as_view(template_name='home.html'), name='home'), # new

]
