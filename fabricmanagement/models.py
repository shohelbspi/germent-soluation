from django.db import models

from django.db import models


# Master Data 

from django.db import models
from django.conf import settings

class Buyer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='buyers_created'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='buyers_updated'
    )

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['email']),
        ]

class Unit(models.Model):
    name = models.CharField(max_length=120, unique=True)
    type = models.CharField(max_length=50)
    location = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='unit_created'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='unit_updated'
    )

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        
class MachineType(models.Model):
    type = models.CharField(unique=True,max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='machine_type_created'
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='machine_type_updated'
    )

    class Meta:
        indexes = [
            models.Index(fields=['type']),
        ]
        

# Order Related Model
class Order(models.Model):
    buyer_name = models.CharField(max_length=255, db_index=True)
    order_no = models.CharField(max_length=255, db_index=True)
    order_type = models.CharField(max_length=255, db_index=True)
    total_order_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    issue_date = models.DateField(db_index=True)
    shipment_date = models.DateField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['issue_date']),
            models.Index(fields=['shipment_date']),
            models.Index(fields=['order_no']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        ]


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_index=True, related_name='items')
    style = models.CharField(max_length=244, db_index=True)
    color = models.CharField(max_length=233, db_index=True)
    fabric_design = models.CharField(max_length=233, db_index=True)
    gsm = models.CharField(max_length=233, db_index=True)
    finish_dia = models.CharField(max_length=233, db_index=True)
    machine_dia = models.CharField(max_length=233, db_index=True)
    machine_type = models.CharField(max_length=233, db_index=True)
    order_item_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['style']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
     
        ]
