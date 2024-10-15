from tkinter.font import names

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cvs/', views.cvs, name='cvs'),
    path('cv/', views.cv, name='main'),
    path('resume/<int:id>', views.resume, name='resume'),
    path('resume/pdf/<int:id>/', views.resume_pdf, name='resume_pdf'),
]