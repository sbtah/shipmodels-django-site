from django.urls import path
from panel import views


app_name = 'panel'


urlpatterns = [
    path('', views.main_panel_view, name='panel'),
    path('login/', views.LoginCustomUserView.as_view(), name='login'),
    path('logout/', views.LogoutCustomUserView.as_view(), name='logout'),


    # Images urls.
    path('image/create/',
         views.ImagePostCreateView.as_view(), name='image-create'),
    path('image/<int:pk>/update/',
         views.ImagePostUpdateView.as_view(), name='image-update'),
    path('image/<int:pk>/delete/',
         views.ImagePostDeleteView.as_view(), name='image-delete'),

    # Orders urls.
    path('orders/',
         views.OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/detail/',
         views.OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/update/',
         views.OrderUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/',
         views.OrderDeleteView.as_view(), name='order-delete')

]
