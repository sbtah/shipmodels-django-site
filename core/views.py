from django.shortcuts import render
from banners.models import AboutBanner
from django.shortcuts import get_object_or_404


def home_view(request):
    """Mini Home view."""

    return render(request, 'home.html', {

    })


def about_view(request):
    """Mini About us view."""

    about_banner = get_object_or_404(AboutBanner, is_active=True)

    return render(request, 'about.html', {
        'about_banner': about_banner,
    })


def cookies_view(request):
    """Cookies policy view."""

    return render(request, 'cookies.html', {

    })


def privacy_policy_view(request):
    """Privacy policy view."""

    return render(request, 'privacy.html', {

    })
