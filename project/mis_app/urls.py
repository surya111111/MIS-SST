from django.urls import path
from . import views

urlpatterns = [
    path('batch/', views.batch, name='batch'),
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('batch/<int:id>/', views.batch_detail, name='batch_detail'),
    path('center/', views.center, name='center'),

]
