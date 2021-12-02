from django.forms.fields import JSONField
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import CustomerForm, JobCardForm
from .models import JobCard, Customer
# Create your views here.

@login_required
def dashboard(request):
    context = {'segment': 'dashboard'}
    html_template = loader.get_template('dashboard/dashboard.html')
    return HttpResponse(html_template.render(context,request))


@login_required
def create_job_card(request):

    if request.method == "POST":
        customer_form = CustomerForm(data=request.POST)
        job_card_form = JobCardForm(data=request.POST)

        get_invoice_no = request.POST['invoice_no']
        get_part_number = request.POST.getlist('part_number')
        get_part_name = request.POST.getlist('part_name')
        get_quantity = request.POST.getlist('quantity')
        get_price = request.POST.getlist('price')
        get_total = request.POST.getlist('total')
        get_grand_total = request.POST['grand_total']

        if customer_form.is_valid() and job_card_form.is_valid():
        
            customer_save = customer_form.save(commit=False)
            customer_save.user_id = request.user.id 
            customer_save.save()
            
            # job_save = job_card_form.save(commit=False)
            # job_save.customer_id = customer_save.id
            # job_save.save()

            for a,b,c,d,e in zip(get_part_number,get_part_name, get_quantity,get_price,get_total):
                JobCard.objects.create(customer_id=customer_save.id, invoice_no=get_invoice_no, part_number=a,part_name=b, quantity=c, price=d, total=e, grand_total=get_grand_total)

    else:
        customer_form = CustomerForm()
        job_card_form = JobCardForm()

    return render(request, 'dashboard/jobcard.html',{'customer':customer_form,'jobcard':job_card_form})


def listJobCard(request):

    get_customer = Customer.objects.all()
    get_jobcard = JobCard.objects.all()

    return render(request, 'dashboard/tables.html',{'get_customer':get_customer,'get_jobcard':get_jobcard} )