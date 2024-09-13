from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from fabricmanagement.models import Buyer 
from fabricmanagement.forms import BuyerForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin




class BuyerListView(LoginRequiredMixin,ListView):
    model = Buyer
    template_name = 'buyer/index.html'
    paginate_by = 10
    login_url = reverse_lazy('admin_singin')

    def get_queryset(self):

        filter_username = self.request.GET.get('username', '')

        queryset = Buyer.objects.all()

        if filter_username:
            queryset = queryset.filter(name__icontains=filter_username)

        return queryset
    
class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'buyer/create.html'
    success_url = reverse_lazy('buyer_list') 

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        
        messages.success(self.request, "Buyer created successfully!")
        
        return response
    
class BuyerDetailView(DetailView):
    model = Buyer
    template_name = 'buyer/show.html'

class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'buyer/edit.html'
    success_url = reverse_lazy('buyer_list') 
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user  
        messages.success(self.request, f"Buyer {form.instance.name} was updated successfully!")  
        return super().form_valid(form)

class BuyerDeleteView(DeleteView):
    model = Buyer
    success_url = reverse_lazy('buyer_list')
