from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'all_users', views.Users_viewset, 'Users')

# Users
all_users = views.Users_viewset.as_view({
    'get': 'all_users'
})
new_user = views.Users_viewset.as_view({
    'post': 'new_user'
})
user_id = views.Users_viewset.as_view({
    'get': 'user_id'
})

# Orders
order_id = views.Orders_viewset.as_view({
    'get': 'order_id'
})
new_order = views.Orders_viewset.as_view({
    'post': 'new_order'
})
orders = views.Orders_viewset.as_view({
    'get': 'order_arg'
})
order_by_user = views.Orders_viewset.as_view({
    'get': 'order_by_user'
})


urlpatterns = [
    path('', include(router.urls)),
    path('users/all/', all_users, name='all_users'),
    path('users/new/', new_user, name='new_user'),
    path('users/<user_id>/', user_id, name='user_id'),

    # This one takes care of:
    # multiple order_id and dates
    path('orders/<int:order_id>/', order_id, name='order_id'),
    path('orders/new/', new_order, name='new_order'),
    path('orders/<str:arg>/', orders, name='orders'),
    path('orders/user/<int:user_id>/', order_by_user, name='order_by_user'),



    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
