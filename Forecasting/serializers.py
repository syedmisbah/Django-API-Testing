from . import models

from rest_framework import serializers


class BaseTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BaseTable
        fields = (
            'slug', 
            'name', 
            'created', 
            'last_updated', 
            'CustomerID', 
            'Account', 
        )


