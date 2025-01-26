from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import Customer

# Create your views here.
def customers(request):
    mycustomers = Customer.objects.all().values()
    template = loader.get_template('customers.html')
    context = {
        'mycustomers' : mycustomers,
    }
    return HttpResponse(template.render(context, request))

def customer_details(request, id):
    mycustomer = Customer.objects.get(id=id)
    template = loader.get_template('customer_details.html')
    context = {
        'mycustomers': mycustomer
    }
    return HttpResponse(template.render(context, request))