from django.http import Http404
from django.shortcuts import render

from .models import Contact, Student

def detail(request, id):
    try:
        item = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'detail.html', {'item': item, 'title': 'Contact Detail'})


def student_detail(request, id):
    try:
        item = Student.objects.get(pk=id)
    except Contact.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'student_detail.html', {'item': item, 'title': 'Student Detail'})


def index(request):
    return render(request, 'index.html', {'item_list': Contact.objects.all(), 'title': 'HOME'})


def student(request):
    return render(request, 'student.html', {'item_list': Student.objects.all(), 'title': 'Students'})

#
# def index_long(request):
#
#     item_list = Contact.objects.all()
#
#     context = {
#         'item_list': item_list,
#         'title': 'MIS'
#     }
#
#     template = loader.get_template('index.html')
#     response = template.render(context, request)
#     return HttpResponse(response)
#     # return render(request, 'index.html', context={'title': 'MIS'})

