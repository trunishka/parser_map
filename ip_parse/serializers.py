from rest_framework import serializers
from ip_parse.models import Compromized_IP

class CompromizedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compromized_IP
        fields = "__all__"