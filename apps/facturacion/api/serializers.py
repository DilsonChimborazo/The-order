from rest_framework.serializers import ModelSerializer
from apps.facturacion.models import Facturacion

class FacturacionSerializer(ModelSerializer):
    class Meta:
        model = Facturacion
        fields = ['pedido', 'detalle', 'total_a_pagar']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['pedido'] = instance.pedido.nombre_pedido
        representation['detalle'] = {
            'producto': instance.detalle.producto.nombre,
            'cantidad': instance.detalle.cantidad,
            'total': instance.total_a_pagar()
        }
        return representation