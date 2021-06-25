from rest_framework import serializers
from .models import Snack


# class SnackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snack
#         fields = "__all__"

# from rest_framework import serializers
# from .models import CookieStand


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = (
            'id',
            "location",
            'owner',
            'description',
            'hourly_sales',
            'minimum_customers_per_hour',
            'maximum_customers_per_hour',
            'average_snack_per_sale',
            )