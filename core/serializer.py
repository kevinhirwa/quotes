from rest_framework import serializers
from . models import *

class ReactSerialzer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['name','detail']