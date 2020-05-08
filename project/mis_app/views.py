from django.http import Http404
from django.shortcuts import render

from .models import Contact,Batch,CenterSite

def detail(request, id):
    try:
        item = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'detail.html', {'item': item, 'title': 'Contact Detail'})


def batch_detail(request, id):
    try:
        item = Batch.objects.get(pk=id)
    except Contact.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'batch_detail.html', {'item': item, 'title': 'Batch Detail'})


def home(request):
    return render(request, 'home.html', {'title': 'HOME'})


def batch(request):
    return render(request, 'batch.html', {'item_list': Batch.objects.all(), 'title': 'Batch'})


def center(request):
    return render(request, 'center.html', {'center': CenterSite.objects.all().first(), 'title': 'Center'})


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

