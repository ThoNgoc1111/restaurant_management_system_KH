from django.contrib import admin
from core.models import MenuItem, Order, OrderItem, Reservation, Payment, Statistic, NotificationService

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Statistic)
admin.site.register(NotificationService)