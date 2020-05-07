# serializers.py
from rest_framework import serializers
from myapi.views import *
from myapi.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IpcSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPC
        fields = '__all__'