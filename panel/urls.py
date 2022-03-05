from django.urls import path
from panel import views


app_name = 'panel'


urlpatterns = [
    path('', views.main_panel_view, name='panel'),
    path('login/', views.LoginCustomUserView.as_view(), name='login'),
    path('logout/', views.LogoutCustomUserView.as_view(), name='logout'),
    path('image-create/', views.ImagePostCreateView.as_view(), name='image-create'),
    path('order-list/', views.OrderListView.as_view(), name='order-list'),
    path('order-detail/<int:pk>/',
         views.OrderDetailView.as_view(), name='order-detail'),
    path('order-update/<int:pk>/',
         views.OrderUpdateView.as_view(), name='order-update'),
    path('order-delete/<int:pk>/',
         views.OrderDeleteView.as_view(), name='order-delete')

]
