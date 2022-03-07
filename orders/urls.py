from django.urls import path
from orders import views
from django.utils.translation import gettext_lazy as _


app_name = 'orders'


urlpatterns = [
    path(_('dodaj/'), views.OrderCreateView.as_view(), name='order-create'),
]
