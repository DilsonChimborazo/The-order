from rest_framework.serializers import ModelSerializer
from apps.detalles.models import DetallePedido

class DetallePedidoSerializer(ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'