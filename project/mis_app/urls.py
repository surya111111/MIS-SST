from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student, name='student'),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),

]
