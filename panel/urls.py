from django.urls import path
from panel import views


app_name = 'panel'


urlpatterns = [
    path('login/', views.LoginCustomUserView.as_view(), name='login'),
    path('logout/', views.LogoutCustomUserView.as_view(), name='logout'),
]
