from django.shortcuts import render, redirect
from django.views import View
from core.models import Order
from django.contrib import messages
from customers.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@staff_member_required
def admin_order_review(request):
    orders = Order.objects.all()
    return render(request, 'admin_order_review.html', {'orders': orders})

class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
class CustomLogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'registration/logout.html')

    @method_decorator(login_required)
    def post(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))
    
@login_required
def home(request):
    return render(request, 'core/home.html')