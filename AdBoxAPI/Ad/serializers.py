
from rest_framework import serializers


class AdListSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)


class AdSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)

class AdCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=7, decimal_places=2)
    description = serializers.CharField(max_length=1000)
    data_create = serializers.DateTimeField(read_only=True)



