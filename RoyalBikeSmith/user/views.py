from django.forms.fields import JSONField
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import CustomerForm, JobCardForm, UserRegistrationForm
from .models import JobCard, Customer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

        get_part_number = request.POST.getlist('part_number')
        get_part_name = request.POST.getlist('part_name')
        get_quantity = request.POST.getlist('quantity')
        get_price = request.POST.getlist('price')
        get_total = request.POST.getlist('total')
        

        if customer_form.is_valid() and job_card_form.is_valid():
        
            customer_save = customer_form.save(commit=False)
            customer_save.user_id = request.user.id 
            customer_save.save()
                    
                    # job_save = job_card_form.save(commit=False)
                    # job_save.customer_id = customer_save.id
                    # job_save.save()

            for a,b,c,d,e in zip(get_part_number,get_part_name, get_quantity,get_price,get_total):
                JobCard.objects.create(customer_id=customer_save.id, part_number=a,part_name=b, quantity=c, price=d, total=e)
            
    else:
        customer_form = CustomerForm()
        job_card_form = JobCardForm()

    return render(request, 'dashboard/jobcard.html',{'customer':customer_form,'jobcard':job_card_form})


def listJobCard(request):

    get_customer = Customer.objects.all()
    page = request.GET.get('page',1)


    paginator = Paginator(get_customer, 8)
    
    try:
        customer = paginator.page(page)

    except PageNotAnInteger:
        customer = paginator.page(1)

    except EmptyPage:
        customer = paginator.page(paginator.num_pages)



    return render(request, 'dashboard/tables.html',{'get_customer':customer,} )

def detailView(request, id):

    get_customer = Customer.objects.get(pk = id)
    get_jobCard = JobCard.objects.filter(customer_id = id)

    return render(request, 'dashboard/detailView.html',{'customer':get_customer,'jobcard':get_jobCard})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'dashboard/register_done.html',{'new_user': new_user})
        
    else:
        user_form = UserRegistrationForm()

    return render(request, 'dashboard/register.html',{'user_form': user_form})