from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')
    return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_emAlta(request):
    lista_filmes = Filme.objects.all().order_by('-vizualizacoes')
    return {"lista_filmes_emAlta": lista_filmes}