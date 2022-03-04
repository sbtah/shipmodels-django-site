from django.views import generic
from django.urls import reverse
from orders.models import Order
from orders.forms import OrderForm
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
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

    def get_success_url(self):
        return reverse('home')
