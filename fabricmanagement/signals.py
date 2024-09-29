
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import KnitCard, Order, OrderItem
from decimal import Decimal


@receiver(post_save, sender=KnitCard)
def update_order_quantities(sender, instance, created, **kwargs):
    if created:
        order_item = instance.order_item
        order_item.total_assign_qty += Decimal(instance.knitcard_qty)
        order_item.save()

        order = order_item.order_id
        order.total_knitcard_qty += Decimal(instance.knitcard_qty)
        order.save()

@receiver(post_delete, sender=KnitCard)
def update_order_quantities_on_delete(sender, instance, **kwargs):
    order_item = instance.order_item
    order_item.total_assign_qty -= Decimal(instance.knitcard_qty)
    order_item.save()

    order = order_item.order
    order.total_knitcard_qty -= Decimal(instance.knitcard_qty)
    order.save()