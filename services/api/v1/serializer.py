from rest_framework import serializers
from services.models import Services


class Serviceserializer(serializers.ModelSerializer):
    model = Services
    fields = ['title','content']