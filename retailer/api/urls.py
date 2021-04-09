from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.Users_viewset, 'Users')


users = views.Users_viewset.as_view({
    'get': 'all_users',
    'post': 'new_user'
})

user_id = views.Users_viewset.as_view({
    'get': 'user_id'
})


urlpatterns = [
    path('', include(router.urls)),
    path('users/', users, name='user'),
    path('users/<user_id>/', user_id, name='user_id'),



    # TODO: Revisar a fondo el funcionamiento de esto
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('users/<int:id>/', views.UsersViewSet)

    
    # TODO
    # path('orders/[order_ids]/', admin.site.urls),
    # path('orders/date-start - date-end/', admin.site.urls),
    # path('orders/shipping/{key=string}/', admin.site.urls),

    # path('orders/user/<int:user_id>/', admin.site.urls),
    # path('users/all/', admin.site.urls),
    # path('users/<int:user_id>/', admin.site.urls),

    # path('orders/search term/', admin.site.urls),
]
