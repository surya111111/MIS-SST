from django.urls import path
from . import views

urlpatterns = [
    path('batch/', views.batch, name='batch'),
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('batch/<int:id>/', views.batch_detail, name='batch_detail'),
    path('center/', views.center, name='center'),
    path('employer/', views.employer, name='employer'),
    path('employer/<int:id>/', views.employer_detail, name='employer_detail'),
    path('exam/', views.exam, name='exam'),
    path('exam/<int:id>/', views.exam_detail, name='exam_detail'),
    path('holiday/', views.holiday, name='holiday'),
    path('holiday/<int:id>/', views.holiday_detail, name='holiday_detail'),
    path('payment/', views.payment, name='payment'),
    path('payment/<int:id>/', views.payment_detail, name='payment_detail'),
    path('placement/', views.placement, name='placement'),
    path('placement/<int:id>/', views.placement_detail, name='placement_detail'),
]
