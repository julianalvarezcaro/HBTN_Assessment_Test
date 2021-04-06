from rest_framework import serializers

from .models import Orders, Payments, Shippings, Users

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ('order_id', 'date', 'total', 'subtotal', 'taxes', 'paid', 'user')

class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payments
        fields = ('payment_id', 'type', 'date', 'txn_id', 'total', 'status', 'order')

class ShippingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shippings
        fields = ('ship_id', 'address', 'city', 'state', 'country', 'cost', 'order')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'name', 'last_name', 'gov_id', 'email', 'company')
