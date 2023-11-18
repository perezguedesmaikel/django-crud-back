from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .serializers import ProductoSerializer
from .models import Producto


class ProductoDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()


class ProductoListCreateView(ListCreateAPIView):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
