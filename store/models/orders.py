from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
        
    def __str__(self):
        status="Pending"
        if self.status:
            status="Completed"
        return str(str(self.id)+"   -Date   -"+str(self.date)+"    -"+status)

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

