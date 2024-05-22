from .models import Producto 
#Estoy asumiendo que la clase Producto esta en un archivo models en este mismo directorio

from django.views.generic.list import ListView

class ProductoListView(ListView):
    model = Producto
    paginate_by = 10
    