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
def page(request):
    context = {}
    # All resource path end in .html
    # Pick out the html file name from the url. and load that template.

    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('dashboard/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('dashboard/page-404.html')
        return HttpResponse(html_template.render(context,request))

    except:
        html_template = loader.get_template('dashboard/page-500.html')
        return HttpResponse(html_template.render(context, request))


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


    return render(request, 'test.html',{'customer':customer_form, 'jobcard':job_card_form})

