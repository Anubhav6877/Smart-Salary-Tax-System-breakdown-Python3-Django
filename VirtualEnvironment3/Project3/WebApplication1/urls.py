from django.urls import path
from . import views

urlpatterns = [
    path('', views.salary_view, name='salary'),
]

