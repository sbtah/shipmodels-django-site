from django.shortcuts import render
from orders.models import Order
from orders.forms import OrderForm
from gallery.models import ImageGallery, ImagePost
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from users.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


@login_required
def main_panel_view(request):
    """View for admin panel."""

    orders = Order.objects.all()
    orders_count = orders.count()
    galleries = ImageGallery.objects.all()
    galleries_count = galleries.count()

    return render(request, 'panel/admin_panel.html', {
        'orders': orders,
        'galleries': galleries,
        'orders_count': orders_count,
        'galleries_count': galleries_count,
    })


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
    success_message = "Your are logged out"
