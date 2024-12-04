from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # New field for image

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.menu_item.name}"

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)  # Add this field
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation by {self.user.username} on {self.date} at {self.time}"

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment for Order {self.order.id}"

class Statistic(models.Model):
    statistic_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    sales_count = models.IntegerField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Statistics for {self.item.name}"

class NotificationService(models.Model):
    notification_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, null=True, blank=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.customer.username}"