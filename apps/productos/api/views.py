from rest_framework.Viewset import ModelViewSet
from apps.productos.models import Productos
from apps.productos.api.serializers import ProductosSerializer

class ProductosSerializer(ModelViewSet):
    serializer_class= ProductosSerializer
    queryset = Productos.objects.all()
    http_method_names=['get', 'post', 'put', 'patch']