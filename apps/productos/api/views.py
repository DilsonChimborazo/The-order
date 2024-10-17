from rest_framework.viewsets import ModelViewSet
from apps.productos.models import Producto
from apps.productos.api.serializers import ProductosSerializer

class ProductosModelViewSet(ModelViewSet):
    serializer_class= ProductosSerializer
    queryset = Producto.objects.all()