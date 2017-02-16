from rest_framework import serializers
from ip_parse.models import CompromizedIP

class CompromizedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompromizedIP
        fields = "__all__"