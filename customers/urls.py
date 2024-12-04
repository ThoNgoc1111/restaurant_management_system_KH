from django.urls import path
from .views import register, admin_order_review, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('admin/orders/', admin_order_review, name='admin_order_review'),
]