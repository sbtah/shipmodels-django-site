from django.shortcuts import render
from gallery.forms import ImagePostForm
from orders.models import Order
from orders.forms import OrderForm
from gallery.models import ImageGallery, ImagePost
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserAuthenticationForm
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


@login_required
def main_panel_view(request):
    """View for admin panel."""

    orders = Order.objects.all()
    orders_count = orders.count()
    images = ImagePost.objects.all()
    images_count = images.count()
    galleries = ImageGallery.objects.all()
    galleries_count = galleries.count()

    return render(request, 'panel/admin_panel.html', {
        'orders': orders,
        'galleries': galleries,
        'orders_count': orders_count,
        'galleries_count': galleries_count,
        'images': images,
        'images_count': images_count,
    })


# User related views.
class LoginCustomUserView(SuccessMessageMixin, LoginView):
    """Class based view for login in users."""

    authentication_form = CustomUserAuthenticationForm
    template_name = 'panel/login_user.html'
    next_page = 'home'
    success_message = "Your are logged in"


class LogoutCustomUserView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
    """Class based view to logout users."""

    template_name = 'panel/logout_user.html'
    success_url = reverse_lazy('home')
    next_page = 'home'
    success_message = "Your are logged out"


# Order related views. TD - admin create order.
class OrderListView(LoginRequiredMixin, generic.ListView):
    """ListView for Order objects. This view is available for logged users."""

    model = Order
    template_name = 'panel/list_order.html'
    context_object_name = 'orders'


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    """DetailView for Order object, available for logged in users."""

    model = Order
    template_name = 'panel/detail_order.html'
    context_object_name = 'order'


class OrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    """UpdateView for Order object for logged users only."""

    model = Order
    form_class = OrderForm
    template_name = 'panel/update_order.html'
    success_url = reverse_lazy('panel:panel')


class OrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    """DeleteView for order object. Available for logged in users."""

    model = Order
    template_name = 'panel/delete_order.html'
    success_url = reverse_lazy('panel:panel')


# ImagePost related views.
class ImagePostCreateView(LoginRequiredMixin, generic.CreateView):
    """CreateView for ImagePost object - for logged users only."""

    model = ImagePost
    form_class = ImagePostForm
    template_name = 'panel/create_image.html'
    success_url = reverse_lazy('panel:panel')
    success_message = _("Obraz dodany")


class ImagePostUpdateView(LoginRequiredMixin, generic.UpdateView):
    """Update view for ImagePost object - only for logged users."""

    model = ImagePost
    form_class = ImagePostForm
    template_name = 'panel/update_image.html'
    success_message = _("Zmiany wykonane")
    success_url = reverse_lazy('panel:panel')


class ImagePostDeleteView(LoginRequiredMixin, generic.DeleteView):
    """DeleteView for ImagePost object - only for logged users."""

    model = ImagePost
    template_name = 'panel/delete_image.html'
    success_message = _("Obraz usunięty")
    success_url = reverse_lazy('panel:panel')
