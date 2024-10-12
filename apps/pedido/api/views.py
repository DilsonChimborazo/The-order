from rest_framework.viewsets import ModelViewSet
from apps.pedido.models import Pedidos
from apps.pedido.api.serializers import PedidoSerializer

class PedidoModelViewset(ModelViewSet):
    serializer_class= PedidoSerializer
    queryset = Pedidos.objects.all()
    http_method_names=['get', 'post', 'put', 'delete', 'patch']