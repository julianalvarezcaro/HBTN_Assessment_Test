from django.contrib import admin
from .models import Orders, Payments, Shippings, Users

admin.site.register(Orders)
admin.site.register(Payments)
admin.site.register(Shippings)
admin.site.register(Users)
