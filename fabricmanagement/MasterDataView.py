from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from fabricmanagement.models import Buyer,Unit,MachineType,Machine
from fabricmanagement.forms import BuyerForm,UnitForm,MachineTypeForm,MachineForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



# Buyer

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

# Unit
class UnitListView(LoginRequiredMixin,ListView):
    model = Unit
    template_name = 'unit/index.html'
    paginate_by = 10
    login_url = reverse_lazy('admin_singin')

    def get_queryset(self):

        filter_name = self.request.GET.get('name', '')
        filter_type = self.request.GET.get('type', '')
        filter_location = self.request.GET.get('location', '')

        queryset = Unit.objects.all()

        if filter_name:
            queryset = queryset.filter(name__icontains=filter_name)
        if filter_type:
            queryset = queryset.filter(type__icontains=filter_type)
        if filter_location:
            queryset = queryset.filter(location__icontains=filter_location)

        return queryset
    
class UnitCreateView(CreateView):
    model = Unit
    form_class = UnitForm
    template_name = 'unit/create.html'
    success_url = reverse_lazy('unit_list') 

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        
        messages.success(self.request, "Unit created successfully!")
        
        return response
    
class UnitDetailView(DetailView):
    model = Unit
    template_name = 'unit/show.html'

class UnitUpdateView(UpdateView):
    model = Unit
    form_class = UnitForm
    template_name = 'unit/edit.html'
    success_url = reverse_lazy('unit_list') 
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user  
        messages.success(self.request, f"Unit {form.instance.name} was updated successfully!")  
        return super().form_valid(form)

    
class UnitDeleteView(DeleteView):
    model = Unit
    success_url = reverse_lazy('unit_list')

    def delete(self, request, *args, **kwargs):
        unit = self.get_object()
        messages.success(self.request, f'Unit "{unit.name}" was successfully deleted.')
        return super().delete(request, *args, **kwargs)


# Machine Type

class MachineTypeListView(LoginRequiredMixin,ListView):
    model = MachineType
    template_name = 'machine-type/index.html'
    context_object_name = 'machine_types'
    paginate_by = 10
    login_url = reverse_lazy('admin_singin')

    def get_queryset(self):

        filter_type = self.request.GET.get('type', '')

        queryset = MachineType.objects.all()

        if filter_type:
            queryset = queryset.filter(type__icontains=filter_type)

        return queryset
    
class MachineTypeCreateView(CreateView):
    model = MachineType
    form_class = MachineTypeForm
    template_name = 'machine-type/create.html'
    success_url = reverse_lazy('machine_type_list') 

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        
        messages.success(self.request, "Machine Type created successfully!")
        
        return response
    
class MachineTypeDetailView(DetailView):
    model = MachineType
    template_name = 'machine-type/show.html'
    context_object_name = 'machine_type'


class MachineTypeUpdateView(UpdateView):
    model = MachineType
    form_class = MachineTypeForm
    template_name = 'machine-type/edit.html'
    context_object_name = 'machine_type'

    success_url = reverse_lazy('machine_type_list') 
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user  
        messages.success(self.request, f"{form.instance.type} was updated successfully!")  
        return super().form_valid(form)

    
class MachineTypeDeleteView(DeleteView):
    model = MachineType
    success_url = reverse_lazy('machine_type_list')


# Machine

class MachineListView(LoginRequiredMixin,ListView):
    model = Machine
    template_name = 'machine/index.html'
    paginate_by = 10
    login_url = reverse_lazy('admin_singin')

    def get_queryset(self):

        filter_machine_no = self.request.GET.get('machine_no', '')

        queryset = Machine.objects.all()

        if filter_machine_no:
            queryset = queryset.filter(machine_no__icontains=filter_machine_no)

        return queryset

class MachineCreateView(CreateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine/create.html'
    success_url = reverse_lazy('machine_list') 

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        
        messages.success(self.request, "Machine created successfully!")
        
        return response

class MachineDetailView(DetailView):
    model = Machine
    template_name = 'machine/show.html'


class MachineUpdateView(UpdateView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine/edit.html'

    success_url = reverse_lazy('machine_list') 
    
    def form_valid(self, form):
        form.instance.updated_by = self.request.user  
        messages.success(self.request, f"Machine {form.instance.machine_no} was updated successfully!")  
        return super().form_valid(form)

    
class MachineDeleteView(DeleteView):
    model = Machine
    success_url = reverse_lazy('machine_list')

