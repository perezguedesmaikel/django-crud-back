
from rest_framework.viewsets import ModelViewSet

from .serializers import ProductoSerializer
from .models import Producto


class ProductCrud(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
