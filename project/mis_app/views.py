from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# from django.shortcuts import render

# Create your views here.
from .models import Contact


def index(request):
    item_list = Contact.objects.all()
    template = loader.get_template('index.html')
    context = {
        'item_list': item_list,
        'title': 'MIS'
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'index.html', context={'title': 'MIS'})

def detail(request, id):
    try:
        item = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'detail.html', {'item': item})
