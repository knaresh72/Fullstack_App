from django.urls import path
from .views import (CategoryListCreateView,CategoryDetailView, ProductListCreateView,ProductDetailView,
                    UserListCreateView,UserDetailView, OrderListCreateView,OrderDetailView)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('Products/<int:pk>/', ProductDetailView.as_view(), name='Products-details'),
    path('Users/<int:pk>/', UserDetailView.as_view(), name='users-details'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='orders-details'),

]
