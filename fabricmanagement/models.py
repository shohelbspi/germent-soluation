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
    
    def __str__(self):
        return self.name 
    
        
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
    def __str__(self):
        return self.type 

class Machine(models.Model):
    machine_no                  = models.PositiveIntegerField(unique=True)
    unit                        = models.ForeignKey(Unit, on_delete=models.CASCADE)
    machine_name                = models.CharField(max_length=50)
    machine_brand               = models.CharField(max_length=50)
    machine_gauge               = models.CharField(max_length=50)
    machine_type                = models.ForeignKey(MachineType, on_delete=models.CASCADE)
    machine_dia                 = models.PositiveIntegerField()
    no_of_feeder                = models.PositiveIntegerField()  
    rotation_per_minute         = models.PositiveIntegerField()
    accuracy                    = models.DecimalField(max_digits=5, decimal_places=2)  
    production_capacity_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_maintenance              = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    loaded_status               = models.BooleanField(default=False)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['machine_no']),
            models.Index(fields=['is_active']),
        ]

class YarnCount(models.Model):
    yarn_count = models.CharField(max_length=70,unique=True,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['yarn_count'])
        ]
    def __str__(self):
        return self.yarn_count
    
class YarnType(models.Model):
    yarn_type = models.CharField(max_length=70,unique=True,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['yarn_type'])
        ]
    def __str__(self):
        return self.yarn_type
    


# Order Related Model
class Order(models.Model):
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    order_no = models.CharField(max_length=255, db_index=True)
    order_type = models.CharField(max_length=255, db_index=True)
    total_order_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_knitcard_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_production_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
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
    total_assign_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    total_produce_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    total_store_recv_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    total_store_del_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    total_challan_qty = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['style']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
     
        ]


class YarnOrder(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='yarn_orders')

    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='yarn_orders')

    yarn_count_id = models.ForeignKey(YarnCount, on_delete=models.SET_NULL, null=True, related_name='yarn_orders')
    
    yarn_type_id = models.ForeignKey(YarnType,on_delete=models.SET_NULL, null=True, related_name='yarn_orders')
    yarn_brand = models.CharField(max_length=50)
    yarn_lot = models.CharField(max_length=50)
    stitch_length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_yarn_receive_qty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_yarn_knitted_qty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


