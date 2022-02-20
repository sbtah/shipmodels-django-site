from django.shortcuts import render


def home_view(request):
    """Mini home view."""

    return render(request, 'home.html', {

    })
