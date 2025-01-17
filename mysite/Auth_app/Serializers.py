from rest_framework import serializers
from .models import Contact


# class ContactSerializer(serializers.Serializer):
#     full_name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     mobile_number = serializers.CharField(max_length=10)
#     country = serializers.CharField(max_length=100)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'