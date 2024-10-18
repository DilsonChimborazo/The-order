from rest_framework.viewsets import ModelViewSet
from apps.zona_preparacion.models import ZonaPreparacion
from apps.zona_preparacion.api.serializers import zonaPreparacionSerializer

class zonaPreparacionModelViewSet(ModelViewSet):
    serializer_class= zonaPreparacionSerializer
    queryset = ZonaPreparacion.objects.all()