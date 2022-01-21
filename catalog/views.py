from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.


def index(request):
    """View function para a home page do site."""
    
    # Gera a contagem de alguns dos objetos principais
    num_books = Book.objects.all().count()
    num_instances = Book.objects.all().count()
    num_genres = Genre.objects.all().count()
    
    # Livros disponíveis (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # Livro com alguma palavra específica:
    word = 'Outro'
    filter_books_by = Book.objects.filter(title__icontains=word)
    
    # O 'all()' fica implícito como padrão.
    num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'word': word,
        'filter_books_by': filter_books_by
    }
    
    # Renderiza o template HTML (index.html) com os dados da variável 'context':
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # <- variável de template
    queryset = Book.objects.filter(title__icontains='Livro')[:5]  # Pega 5 livros que contém no título a palavra 'Outro'
    template_name = 'books/book_list.html'  # Especifica o nome/localização do template
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book
