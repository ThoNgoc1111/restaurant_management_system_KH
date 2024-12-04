from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from core.models import MenuItem, Order, OrderItem
from django.contrib import messages

class PlaceOrderView(View):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        return render(request, 'orders/menu.html', {'menu_items': menu_items})

    def post(self, request):
        ordered_items = request.POST.getlist('ordered_items')
        # quantities = request.POST.getlist('quantities')

        if not ordered_items:
            messages.error(request, "Please select items and specify quantities.")
            return redirect('place_order')

        order = Order.objects.create(user=request.user)
        
        for item_id in ordered_items:
            menu_item = MenuItem.objects.get(id=item_id)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=1)

        return redirect('order_confirmation', order_id=order.id)
    
class OrderConfirmationView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'orders/order_confirmation.html', {'order': order})

    def post(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        ordered_items = request.POST.getlist('ordered_items')
        quantities = request.POST.getlist('quantities')

        if not ordered_items or not quantities:
            messages.error(request, "Please specify quantities for all items.")
            return redirect('order_confirmation', order_id=order.id)

        total_price = 0

        for item_id, quantity in zip(ordered_items, quantities):
            order_item = OrderItem.objects.get(id=item_id)
            quantity = int(quantity)
            order_item.quantity = quantity
            order_item.save()
            total_price += order_item.menu_item.price * quantity

        order.total_price = total_price
        order.save()

        messages.success(request, "Order updated successfully.")
        return redirect('process_payment', order_id=order.id)
    
    
class HandleIncorrectInputView(View):
    def post(self, request):
        ordered_items = request.POST.getlist('ordered_items')
        quantities = request.POST.getlist('quantities')

        if not ordered_items or not quantities:
            messages.error(request, "Please select items and specify quantities.")
            return redirect('place_order')

        for quantity in quantities:
            if not quantity.isdigit() or int(quantity) <= 0:
                messages.error(request, "Invalid quantity specified.")
                return redirect('place_order')

        # Proceed with order placement if input is correct
        return redirect('place_order')
    
    
class ChangeOrderView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        return render(request, 'orders/update_order.html', {'order': order})

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        action = request.POST.get('action')

        if action == 'delete':
            order.delete()
            messages.success(request, "Order deleted successfully.")
            return redirect('menu')

        ordered_items = request.POST.getlist('ordered_items')
        quantities = request.POST.getlist('quantities')

        order.items.all().delete()
        total_price = 0

        for item_id, quantity in zip(ordered_items, quantities):
            menu_item = MenuItem.objects.get(id=item_id)
            quantity = int(quantity)
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)
            total_price += menu_item.price * quantity

        order.total_price = total_price
        order.save()

        messages.success(request, "Order updated successfully.")
        return redirect('orders/order_confirmation', order_id=order.id)