from django.urls import path
from .views import PaymentProcessingView, PaymentConfirmationView

urlpatterns = [
    path('process_payment/<int:order_id>/', PaymentProcessingView.as_view(), name='process_payment'),
    path('confirmation/<int:payment_id>/', PaymentConfirmationView.as_view(), name='payment_confirmation'),
]