from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    mobile_number = models.IntegerField()
    phone_number = models.IntegerField()
    vechile_name = models.CharField(max_length=150)
    model_name = models.CharField(max_length=150)
    registration_number = models.CharField(max_length=200)
    current_km = models.IntegerField()
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class JobCard(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=150)
    part_name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField()
    total = models.IntegerField()

    def __str__(self):
        return self.part_name


