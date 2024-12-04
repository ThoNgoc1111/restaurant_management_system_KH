from django.urls import path
from payment_processor.views import PaymentProcessingView
from orders.views import PlaceOrderView, OrderConfirmationView

urlpatterns = [
    path('place/', PlaceOrderView.as_view(), name='place_order'),
    path('confirmation/<int:order_id>/', OrderConfirmationView.as_view(), name='order_confirmation'),
    path('update/<int:order_id>/', OrderConfirmationView.as_view(), name='update_order'),
    path('process_payment/<int:order_id>/', PaymentProcessingView.as_view(), name='process_payment'),
]