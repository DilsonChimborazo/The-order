from rest_framework.routers import DefaultRouter
from apps.zona_preparacion.api.views import zonaPreparacionModelViewSet

router_productos = DefaultRouter()
router_productos.register(prefix="zona_preparacion",basename="zona_preparacion",viewset=zonaPreparacionModelViewSet)