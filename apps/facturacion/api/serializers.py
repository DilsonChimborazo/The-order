from rest_framework.serializers import ModelSerializer
from apps.facturacion.models import Facturacion

class FacturacionSerializer(ModelSerializer):
    class Meta:
        model = Facturacion
        fields = '__all__'