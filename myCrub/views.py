from rest_framework.generics import CreateAPIView

from .serializers import ProductoSerializer
from .models import Producto

class ProductoCreateView(CreateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()