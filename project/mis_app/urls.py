from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import Contact


# Serializers define the API representation.
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['first', 'primary_email', 'government_id', 'primary_phone', 'nickname', ]


# ViewSets define the view behavior.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)


urlpatterns = [
    url(r'^api_v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contact/', views.contact, name='contact'),
    path('contact/<int:id>/', views.contact_detail, name='contact_detail'),

    path('batch/', views.batch, name='batch'),
    path('', views.home, name='home'),
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
