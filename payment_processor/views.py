from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from core.models import Payment, MenuItem, Order, OrderItem
from payment_processor.forms import CardPaymentForm, PayPalPaymentForm, ShippingAddressForm
from django.contrib import messages

class PaymentProcessingView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        card_form = CardPaymentForm()
        paypal_form = PayPalPaymentForm()
        address_form = ShippingAddressForm()
        return render(request, 'payment_processor/payment.html', {
            'order': order,
            'card_form': card_form,
            'paypal_form': paypal_form,
            'address_form': address_form
        })

    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        card_form = CardPaymentForm(request.POST)
        paypal_form = PayPalPaymentForm(request.POST)
        address_form = ShippingAddressForm(request.POST)

        if card_form.is_valid() and address_form.is_valid():
            # Process card payment
            payment, created = Payment.objects.get_or_create(order=order, defaults={'amount': order.total_price, 'successful': True})
            if not created:
                payment.amount = order.total_price
                payment.successful = True
                payment.save()
            order.ordered = True
            order.save()
            messages.success(request, "Payment processed successfully with card.")
            return redirect('payment_confirmation', payment_id=payment.id)

        elif paypal_form.is_valid() and address_form.is_valid():
            # Process PayPal payment
            payment, created = Payment.objects.get_or_create(order=order, defaults={'amount': order.total_price, 'successful': True})
            if not created:
                payment.amount = order.total_price
                payment.successful = True
                payment.save()
            order.ordered = True
            order.save()
            messages.success(request, "Payment processed successfully with PayPal.")
            return redirect('payment_confirmation', payment_id=payment.id)

        messages.error(request, "There was an error with your payment. Please try again.")
        return render(request, 'payment_processor/payment.html', {
            'order': order,
            'card_form': card_form,
            'paypal_form': paypal_form,
            'address_form': address_form
        })

class PaymentConfirmationView(View):
    def get(self, request, payment_id):
        payment = get_object_or_404(Payment, id=payment_id)
        return render(request, 'payment_processor/payment_confirmation.html', {'payment': payment})