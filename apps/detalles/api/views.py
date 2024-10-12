from rest_framework.Viewset import ModelViewSet
from apps.detalles.models import DetallePedido
from apps.detalles.api.serializers import DetallePedidoSerializer

class DetallesModelViewset(ModelViewSet):
    serializer_class= DetallePedidoSerializer
    queryset = DetallePedido.objects.all()
    http_method_names=['get']