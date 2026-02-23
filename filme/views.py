from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here. CBV (Class base views)

class Homepage(TemplateView):
    template_name = 'homepage.html'


class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
    #object_list  (list of objects)

class Detalhesfilmes(DetailView):
    template_name = 'detalhesfilmes.html'
    model = Filme
    #object  (Object)


# Create your views here. FBV (functions base views)
#def homepage(request):
    #return render(request, 'homepage.html')


#def homefilmes(request):
    #context = {}
    #lista_filmes = Filme.objects.all()
    #context['lista_filmes'] = lista_filmes
    #return render(request, 'homefilmes.html', context)