from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext


def translate(language):
    """"""

    current_language = get_language()
    try:
        activate(language)
        text = gettext('Imię i Nazwisko')
    finally:
        activate(current_language)

    return text


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
