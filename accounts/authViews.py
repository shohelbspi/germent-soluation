from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from accounts.forms import UserRegistrationForm
from accounts.models import User
from django.views.generic import ListView,DeleteView,DetailView

def singin(request):
    if not request.user.is_authenticated:
    
        if request.method == 'POST':
            username = request.POST['username'] 
            password = request.POST['password']  

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome to FabTech')
                return HttpResponseRedirect(reverse('dashboard'))  
            else:
                messages.error(request, 'Invalid username or password.')
                return HttpResponseRedirect(reverse('admin_singin'))  
            
        return render(request, 'accounts/auth/singin.html')

    else:
        return HttpResponseRedirect(reverse('dashboard'))



def singout(request):
    logout(request)  
    messages.success(request, 'You have been logged out successfully.')
    return HttpResponseRedirect(reverse('admin_singin')) 


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/master/dashboard.html')
    else:
        return HttpResponseRedirect(reverse('admin_singin'))
    

def singup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully!')
            return HttpResponseRedirect(reverse('user_list'))
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/auth/singup.html', {'form': form})


class user_list(ListView):
    model = User
    template_name = 'accounts/auth/user-list.html'
    paginate_by=15

    def get_queryset(self):

        filter_username = self.request.GET.get('username', '')
        filter_user_type = self.request.GET.get('user_type', '')

        queryset = User.objects.all()

        if filter_username:
            queryset = queryset.filter(username__icontains=filter_username)
        if filter_user_type:
            queryset = queryset.filter(user_type__icontains=filter_user_type)

        return queryset