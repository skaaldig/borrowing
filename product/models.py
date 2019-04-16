from django.db import models
from django.shortcuts import reverse
from django.core.exceptions import ValidationError

from borrowing.users.models import User
from warehouse.models import Warehouse

STATUS = (
    ('m', 'Maintenance'),
    ('o', 'On Loan'),
    ('a', 'Available')
)

class Manufacturer(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):

    model_number = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    human_readable_name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    bin_location = models.CharField(max_length=25)
    loan_status = models.CharField(max_length=1, choices=STATUS)

    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('warehouse.Warehouse', null=True, on_delete=models.CASCADE)
    current_borrower = models.ForeignKey('users.User', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_number

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.pk])


class ProductInstance(models.Model):
    requested = models.DateField(auto_now_add=True)
    rental_end = models.DateField()
    returned = models.DateField(blank=True, null=True)
    return_note = models.TextField(blank=True, null=True, help_text="Where you left the demo and any notes on condition")

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    borrower = models.ForeignKey('users.User', blank=True, on_delete=models.CASCADE)
    returned_to = models.ForeignKey('warehouse.Warehouse', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return f"User: {self.borrower} Date: {self.requested} - {self.rental_end} " \
               f"Product: {self.product.human_readable_name}"

    def get_absoulte_url(self):
        return reverse('product-instance', args=[self.pk])
