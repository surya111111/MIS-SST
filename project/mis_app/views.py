from django.http import Http404
from django.shortcuts import render

from .models import Contact, ContactForm, Batch, CenterSite, Employer, Exam, Holidays, Payment, Placement


def contact(request):
    return render(request, 'contact.html', {'item_list': Contact.objects.all(), 'title': 'Contact List'})


def contact_detail(request, id):
    try:
        item = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        raise Http404("Item does not exist")

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            # Do something. Should generally end with a redirect. For example:
            return contact(request)
    else:
        form = ContactForm(instance=item)

    return render(request, 'contact_detail.html', {'item': item, 'title': 'Contact Detail', 'form': form})


def batch_detail(request, id):
    try:
        item = Batch.objects.get(pk=id)
    except Contact.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'batch_detail.html', {'item': item, 'title': 'Batch Detail'})


def employer_detail(request, id):
    try:
        item = Employer.objects.get(pk=id)
    except Employer.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'employer_detail.html', {'item': item, 'title': 'Employer Detail'})


def home(request):
    return render(request, 'home.html', {'title': 'HOME'})


def batch(request):
    return render(request, 'batch.html', {'item_list': Batch.objects.all(), 'title': 'Batch'})


def center(request):
    return render(request, 'center.html', {'center': CenterSite.objects.all().first(), 'title': 'Center'})


def employer(request):
    return render(request, 'employer.html', {'item_list': Employer.objects.all(), 'title': 'Employer'})


def exam(request):
    return render(request, 'exam.html', {'item_list': Exam.objects.all(), 'title': 'Exam'})


def holiday(request):
    return render(request, 'holiday.html',{'item_list': Holidays.objects.all(), 'title': 'Holidays'})

def payment(request):
    return render(request, 'payment.html',{'item_list': Payment.objects.all(), 'title': 'Payment'})

def payment_detail(request, id):
    try:
        item = Payment.objects.get(pk=id)

    except Payment.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'payment_detail.html', {'item': item, 'title': 'Payment Detail'})

def payment(request):
    return render(request, 'placement.html',{'item_list': Placement.objects.all(), 'title': 'Placement'})

def placement(request):
    return render(request, 'placement.html',{'item_list': Placement.objects.all(), 'title': 'Placement'})

def placement_detail(request, id):
    try:
        item = Placement.objects.get(pk=id)

    except Placement.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'Placement_detail.html', {'item': item, 'title': 'Placement Detail'})


def holiday_detail(request, id):
    try:
        item = Holidays.objects.get(pk=id)

    except Holidays.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'holiday_detail.html', {'item': item, 'title': 'Holiday Detail'})


def exam_detail(request, id):
    try:
        item = Exam.objects.get(pk=id)

    except Exam.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'exam_detail.html', {'item': item, 'title': 'Exam Detail'})


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

