from django.views import generic
from django.urls import reverse
from orders.models import Order
from orders.forms import OrderForm
from django.contrib.messages.views import SuccessMessageMixin


class CreateOrderView(generic.CreateView, SuccessMessageMixin):
    """CreateView for Order object."""

    form_class = OrderForm
    template_name = 'orders/order_create.html'
    success_message = 'Order created, thank you'
    model = Order

    def get_success_url(self):
        return reverse('home')
