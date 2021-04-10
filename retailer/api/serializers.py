from rest_framework import serializers

from .models import Orders, Payments, Shippings, Users

class Orders_serializer(serializers.HyperlinkedModelSerializer):
    # To incluide the FK from another table
    user = serializers.ReadOnlyField(source='user.user_id')
    class Meta:
        model = Orders
        fields = ('order_id', 'date', 'total', 'subtotal', 'taxes', 'paid', 'user')

class Payments_serializer(serializers.HyperlinkedModelSerializer):
    # To incluide the FK from another table
    order = serializers.ReadOnlyField(source='order.order_id')
    class Meta:
        model = Payments
        fields = ('payment_id', 'type', 'date', 'txn_id', 'total', 'status', 'order')

class Shippings_serializer(serializers.HyperlinkedModelSerializer):
    # To incluide the FK from another table
    order = serializers.ReadOnlyField(source='order.order_id')
    class Meta:
        model = Shippings
        fields = ('ship_id', 'address', 'city', 'state', 'country', 'cost', 'order')

class Users_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'name', 'last_name', 'gov_id', 'email', 'company')
