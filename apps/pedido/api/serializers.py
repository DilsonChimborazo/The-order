from rest_framework.serializers import ModelSerializer
from apps.pedido.models import Pedidos

class DetallePedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'