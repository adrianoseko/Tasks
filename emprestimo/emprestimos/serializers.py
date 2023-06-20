from rest_framework import serializers
from .models import Propostas

class PropostasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propostas
        fields = '__all__'