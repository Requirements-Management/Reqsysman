from rest_framework import serializers
from .models import Requirement


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        #fields = ['id', 'description', 'type', 'priority', 'status', 'version']
        fields = ['id', 'description', 'type', 'priority', 'status']

