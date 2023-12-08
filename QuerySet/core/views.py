from django.shortcuts import render
from django.db.models import Count
from .models import Book, Author, Tag, Review, Profile

def query_examples(request):
  
    livros_por_autor = Book.objects.filter(author__name='Sophie Freitas')
    livros_por_tag = Book.objects.filter(tags__name='Ficção')
    autor_por_bio = Author.objects.filter(bio__contains='Laudantium')
    livros_com_avaliacao_alta = Review.objects.filter(rating__gte=4).distinct()
    perfis_especificos = Profile.objects.filter(website__contains='http://freitas.org/')
    livros_sem_avaliacao = Review.objects.exclude(rating__isnull=True)

    # Envie todas as consultas para o template
    context = {
        'questao1': livros_por_autor,
        'questao2': livros_por_tag,
        'questao3': autor_por_bio,
        'questao4': livros_com_avaliacao_alta,
        'questao5': perfis_especificos,
        'questao6': livros_sem_avaliacao,
        
    }

    return render(request, 'core/respostas.html', context)
