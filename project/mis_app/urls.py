from rest_framework.relations import PrimaryKeyRelatedField
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import *
router = routers.DefaultRouter()

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['first', 'primary_email', 'government_id', 'primary_phone', 'nickname', ]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
router.register(r'contact', ContactViewSet)
   
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['subject', ]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
router.register(r'course', CourseViewSet)

class BatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Batch
        fields = ['name','cost','course',]
        
class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
router.register(r'batch', BatchViewSet)

class AttendanceSerializer(serializers.HyperlinkedModelSerializer):
    contact = PrimaryKeyRelatedField(queryset=Contact.objects.all())

    class Meta:
        model = Attendance
        fields = ['id','attended','contact']
        
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    url(r'^api_v1/', include(router.urls)),
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
