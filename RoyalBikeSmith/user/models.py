from django.db import models
from django.conf import settings

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoice_no = models.IntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    mobile_number = models.IntegerField()
    phone_number = models.IntegerField(null=True)
    vechile_name = models.CharField(max_length=150)
    model_name = models.CharField(max_length=150)
    registration_number = models.CharField(max_length=200)
    current_km = models.IntegerField()
    description = models.TextField(null=True)
    work_assigned = models.CharField(max_length=150)
    maintenance_type = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class JobCard(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=150)
    part_name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.part_name


