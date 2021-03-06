from rest_framework import serializers
from ip_parse.models import CompromizedIP
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.serializers import serialize

class CompromizedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompromizedIP
        fields = ("title", "appear_date", "ip_adress", "as_number", "malware_type", "geom")


class CompromizedStock(APIView):
    def get(self, request):
        compromized = CompromizedIP.objects.all()
        serialazer = serialize('geojson', compromized,  geometry_field='point',
          fields=('name',))
        return Response(serialazer)