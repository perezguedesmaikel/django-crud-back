from rest_framework.generics import ListCreateAPIView

from .serializers import ProductoSerializer
from .models import Producto


class ProductoCreateView(ListCreateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
