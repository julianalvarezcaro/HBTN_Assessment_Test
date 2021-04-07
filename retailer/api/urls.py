from django.urls import path
from .views import get_order

urlpatterns = [
    path('orders/<int:id>/', get_order) #TODO: Add function

    
    # TODO
    # path('orders/[order_ids]/', admin.site.urls),
    # path('orders/date-start - date-end/', admin.site.urls),
    # path('orders/shipping/{key=string}/', admin.site.urls),

    # path('orders/user/<int:user_id>/', admin.site.urls),
    # path('users/all/', admin.site.urls),
    # path('users/<int:user_id>/', admin.site.urls),

    # path('orders/search term/', admin.site.urls),
]
