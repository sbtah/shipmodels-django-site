from django.views import generic
from django.urls import reverse, reverse_lazy
from orders.models import Order
from orders.forms import OrderForm
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin


class OrderCreateView(SuccessMessageMixin, generic.CreateView):
    """
    CreateView for Order object.
    This is a public View.
    """

    form_class = OrderForm
    template_name = 'orders/order_create.html'
    success_message = _('Zamówienie złożone, dziękujemy')
    model = Order
    success_url = reverse_lazy('orders:order-create')
