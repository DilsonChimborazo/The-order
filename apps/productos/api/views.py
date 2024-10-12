from rest_framework.viewsets import ModelViewSet
from apps.productos.models import Productos
from apps.productos.api.serializers import ProductosSerializer

class ProductosModelViewSet(ModelViewSet):
    serializer_class= ProductosSerializer
    queryset = Productos.objects.all()
    http_method_names=['get', 'post', 'put', 'patch']