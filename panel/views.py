from orders.models import Order
from orders.forms import OrderForm
from django.contrib.auth import get_user_model
from users.forms import CustomUserAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class LoginCustomUserView(SuccessMessageMixin, LoginView):
    """Class based view for login in users."""

    authentication_form = CustomUserAuthenticationForm
    template_name = 'panel/login_user.html'
    next_page = 'home'
    success_message = "Your are logged in"


class LogoutCustomUserView(SuccessMessageMixin, LogoutView):
    """Class based view to logout users."""

    template_name = 'panel/logout_user.html'
    success_url = reverse_lazy('home')
    success_message = "Your are logged out"
