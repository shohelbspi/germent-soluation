from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DeleteView,DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderItem 
import json
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

def OrderCreate(request):

    return render(request,'fabricmanagement/order-create.html')

@csrf_exempt
def save_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        buyer_name = data.get('buyer_name')
        order_no = data.get('order_no')
        order_type = data.get('order_type')
        total_order_qty = data.get('total_order_qty')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        items = data.get('items')

        order = Order.objects.create(
            buyer_name=buyer_name,
            order_no=order_no,
            order_type=order_type,
            total_order_qty=total_order_qty,
            issue_date=start_date,
            shipment_date=end_date,
        )

        for item in items:
            OrderItem.objects.create(
                order_id=order,
                style=item.get('style'),
                color=item.get('color'),
                fabric_design=item.get('fabric_design'),
                gsm=item.get('gsm'),
                finish_dia=item.get('finish_dia'),
                machine_dia=item.get('machine_dia'),
                machine_type=item.get('machine_type'),
                order_item_qty=item.get('order_qty'),
            )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


class order_list(LoginRequiredMixin,ListView):
    model = Order
    template_name = 'fabricmanagement/order-list.html'
    paginate_by=15
    login_url = reverse_lazy('admin_singin')

    def get_queryset(self):

        filter_buyer = self.request.GET.get('buyer_name', '')
        filter_order = self.request.GET.get('order_no', '')

        queryset = Order.objects.all()

        if filter_buyer:
            queryset = queryset.filter(buyer_name__icontains=filter_buyer)
        if filter_order:
            queryset = queryset.filter(order_no__icontains=filter_order)

        return queryset
    
class OrderDetailView(DetailView):
    model = Order
    template_name = 'fabricmanagement/order_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = self.object.items.all()  
        return context
    
class order_delete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')

def add_yarn(request,id):
    order_item = get_object_or_404(OrderItem, id=id)

    return render(request,'fabricmanagement/add-yarn.html',{
        'item': order_item,
    })