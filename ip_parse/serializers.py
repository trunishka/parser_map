from rest_framework import serializers
from ip_parse.models import CompromizedIP

class CompromizedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompromizedIP
        fields = ("title", "appear_date", "ip_adress", "as_number", "malware_type", "geom")