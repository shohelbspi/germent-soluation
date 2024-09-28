from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DeleteView,DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderItem ,Buyer,YarnCount,YarnType,YarnOrder,Unit,Machine,KnitCard
import json
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator


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
            buyer_id=buyer_name,
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
        order_items = self.object.items.all()  
        
        for item in order_items:
            item.yarn_exists = YarnOrder.objects.filter(order_item=item).exists() 
                
        context['order_items'] = order_items
        return context

class order_delete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')

def add_yarn_view(request, order_id, item_id):
    order = get_object_or_404(Order, id=order_id)
    item = get_object_or_404(OrderItem, id=item_id)
    context = {
        'order': order,
        'item': item,
    }

    return render(request,'fabricmanagement/add-yarn.html',context)

@csrf_exempt
def save_yarn(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            order_id = data.get('order_id')
            order_item_id = data.get('order_item_id')
            yarns = data.get('all_yarns', [])

            if not order_id or not order_item_id:
                return JsonResponse({'success': False, 'error': 'Missing order_id or order_item_id'})

            if not isinstance(yarns, list):
                return JsonResponse({'success': False, 'error': 'Invalid yarn data'})

            for yarn in yarns:
                yarn_count_id = yarn.get('yarn_count')
                yarn_type_id = yarn.get('yarn_type')

                yarn_count_instance = YarnCount.objects.filter(id=yarn_count_id).first()
                yarn_type_instance = YarnType.objects.filter(id=yarn_type_id).first()

                if not yarn_count_instance:
                    return JsonResponse({'success': False, 'error': f'Invalid yarn_count_id: {yarn_count_id}'})
                if not yarn_type_instance:
                    return JsonResponse({'success': False, 'error': f'Invalid yarn_type_id: {yarn_type_id}'})

                YarnOrder.objects.create(
                    order_id=order_id,
                    order_item_id=order_item_id,
                    yarn_count_id=yarn_count_instance,
                    yarn_type_id=yarn_type_instance,
                    yarn_brand=yarn.get('yarn_brand'),
                    yarn_lot=yarn.get('yarn_lot'),
                    stitch_length=yarn.get('stitch_length', None),
                    percentage=yarn.get('percentage', None),
                    total_yarn_receive_qty=yarn.get('total_yarn_receive_qty', None),
                    total_yarn_knitted_qty=yarn.get('total_yarn_knitted_qty', None),
                )

            return JsonResponse({'success': True})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def add_knitcard_view(request, id):
    item = OrderItem.objects.get(id=id)

    if request.method == 'POST':
        # Capture form data
        unit = request.POST.get('unit')
        machine = request.POST.get('machine')
        assign_qty = request.POST.get('assign_qty')
        knitting_start = request.POST.get('knitting_start')
        knitting_end = request.POST.get('knitting_end')
        order_item_id = request.POST.get('order_item_id')

        KnitCard.objects.create(
            unit_id=unit,
            machine_id=machine,
            knitcard_qty=assign_qty,
            knitting_start_date=knitting_start,
            knitting_end_date=knitting_end,
            order_item_id=order_item_id  # Save the order item ID
        )

        messages.success(request, "Knitcard created successfully!")

    return render(request, 'fabricmanagement/add-knitcard.html', {'item': item})


def buyer_search(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('q', '') 
        if query:
            buyers = Buyer.objects.filter(name__icontains=query)[:10] 
        else:
            buyers = Buyer.objects.all()[:10] 
        buyer_list = [{'id': buyer.id, 'text': buyer.name} for buyer in buyers]  
        return JsonResponse({'results': buyer_list})
    
    return JsonResponse({'results': []})



def yarn_count_list(request):
    yarn_counts = YarnCount.objects.all()
    
    data = [{"id": yarn_count.id, "text": yarn_count.yarn_count} for yarn_count in yarn_counts]
    
    return JsonResponse(data, safe=False)

def yarn_type_list(request):
    yarn_types = YarnType.objects.all()
    
    data = [{"id": yarn_type.id, "text": yarn_type.yarn_type} for yarn_type in yarn_types]
    
    return JsonResponse(data, safe=False)

def unit_select2(request):
    units = Unit.objects.all()
    
    data = [{"id": unit.id, "text": unit.name} for unit in units]
    
    return JsonResponse(data, safe=False)

def machine_select2(request):
    machines = Machine.objects.all()
    
    data = [{"id": machine.id, "text": machine.machine_no} for machine in machines]
    
    return JsonResponse(data, safe=False)

