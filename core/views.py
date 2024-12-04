from django.shortcuts import render
from django.db.models import Sum  # Import Sum from django.db.models
from core.models import MenuItem, Statistic

def home(request):
    # Fetch bestseller menu items (e.g., top 5 items based on sales count)
    bestsellers = MenuItem.objects.annotate(sales_count=Sum('statistic__sales_count')).order_by('-sales_count')[:5]
    return render(request, 'home.html', {'bestsellers': bestsellers})