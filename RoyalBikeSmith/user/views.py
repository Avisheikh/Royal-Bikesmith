from django.forms.fields import JSONField
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import CustomerForm, JobCardForm
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

        if customer_form.is_valid() and job_card_form.is_valid():
            customer_form.save()
            job_card_form.save()

    else:
        customer_form = CustomerForm()
        job_card_form = JobCardForm()


    return render(request, 'dashboard/jobcard.html',{'customer':customer_form, 'jobcard':job_card_form})

