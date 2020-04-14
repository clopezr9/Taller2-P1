from rest_framework import serializers
from .models import Temphum

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temphum
        fields = ('id', 'type', 'value')
