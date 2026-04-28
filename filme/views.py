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

    def get(self, request, *args, **kwargs):
        # verificar o filme que esta sendo acessado
        filme = self.get_object()
        # adicionar uma vizualizacao nesta pagina
        filme.vizualizacoes += 1
        # salvar
        filme.save()
        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final


    def get_context_data(self, **kwargs):
        context = super(Detalhesfilmes, self).get_context_data(**kwargs)
        # Filtrar a categoria dos filmes cuja a categoria é igual a categoria do filme da pagina (context)
        # self.get_object()
        filmes_relacionados = self.model.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class Pesquisafilme(ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            object_list = self.model.objects.all()
            return object_list



# Create your views here. FBV (functions base views)
#def homepage(request):
    #return render(request, 'homepage.html')


#def homefilmes(request):
    #context = {}
    #lista_filmes = Filme.objects.all()
    #context['lista_filmes'] = lista_filmes
    #return render(request, 'homefilmes.html', context)