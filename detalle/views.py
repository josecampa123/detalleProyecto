from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class DetalleListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'desc'

class DetalleDetailView(DetailView):
    model = Post
    template_name = 'detalleDetalle.html'
    context_object_name = 'desc'