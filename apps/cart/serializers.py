from rest_framework import serializers

from apps.cart.models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.title")
    price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2)
    line_total = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ["id", "product_id", "product_name", "price", "quantity", "line_total"]

    def get_line_total(self, obj):
        return obj.quantity * obj.product.price


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    def get_total_price(self, cart):
        return sum(item.quantity * item.product.price for item in cart.items.all())
