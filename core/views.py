from django.shortcuts import render


def home_view(request):
    """Mini Home view."""

    return render(request, 'home.html', {

    })


def about_view(request):
    """Mini About us view."""

    return render(request, 'about.html', {

    })


def cookies_view(request):
    """Cookies policy view."""

    return render(request, 'cookies.html', {

    })


def privacy_policy_view(request):
    """Privacy policy view."""

    return render(request, 'privacy.html', {

    })
