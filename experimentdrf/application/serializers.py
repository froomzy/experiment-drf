from rest_framework import serializers
from . import models


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = [
            'first_name',
            'surname',
            'year',
            'declaration',
            'declaration_date',
        ]
